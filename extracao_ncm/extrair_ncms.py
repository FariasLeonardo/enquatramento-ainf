import pdfplumber
import re
import json

def extrair_ncms(pdf_path, anexo_i_pages=(4, 59), anexo_ii_pages=(60, 62)):
    """
    Extrai NCMs dos Anexos I e II do Convênio ICMS 52/91.
    :param pdf_path: Caminho para o PDF.
    :param anexo_i_pages: Tuple com a página inicial e final do Anexo I.
    :param anexo_ii_pages: Tuple com a página inicial e final do Anexo II.
    :return: Lista de dicionários com NCMs, itens, descrições e anexo.
    """
    ncms = []
    current_item = None
    current_anexo = None

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Determinar qual anexo estamos processando
            if anexo_i_pages[0] <= page_num <= anexo_i_pages[1]:
                current_anexo = "Anexo I"
            elif anexo_ii_pages[0] <= page_num <= anexo_ii_pages[1]:
                current_anexo = "Anexo II"
            else:
                continue

            # Extrair texto da página
            texto = page.extract_text() or ""
            # Dividir em linhas
            linhas = texto.split("\n")

            for linha in linhas:
                # Regex para NCMs (e.g., 1234.56, 1234.56.78, 1234.56.7890)
                ncm_matches = re.findall(r"\d{4}\.\d{2}(?:\.\d{2}(?:\.\d{2,4})?)?", linha)
                # Regex para número do item (e.g., "1", "4.1", "02.a")
                item_match = re.match(r"(\d+\.?\d*|[0-9]{2}\.[a-z])", linha)

                if item_match:
                    current_item = item_match.group(0)

                if ncm_matches:
                    # Extrair descrição (texto após o NCM até o final da linha)
                    descricao = re.sub(r"\d{4}\.\d{2}(?:\.\d{2}(?:\.\d{2,4})?)?", "", linha).strip()
                    # Remover número do item da descrição, se presente
                    if current_item:
                        descricao = re.sub(rf"^{current_item}\s*", "", descricao).strip()

                    for ncm in ncm_matches:
                        ncms.append({
                            "ncm": ncm,
                            "item": current_item or "N/A",
                            "descricao": descricao or "Sem descrição",
                            "anexo": current_anexo
                        })

    return ncms

def salvar_ncms(ncms, output_file):
    """
    Salva os NCMs extraídos em um arquivo JSON.
    :param ncms: Lista de dicionários com NCMs.
    :param output_file: Caminho para o arquivo de saída.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(ncms, f, ensure_ascii=False, indent=2)
    print(f"Salvos {len(ncms)} NCMs em {output_file}")

# Configurações
PDF_PATH = "convenio_icms_52_91.pdf"  # Ajuste para o nome do seu PDF
OUTPUT_FILE = "ncms.json"

# Executar extração
ncms_extraidos = extrair_ncms(PDF_PATH)
salvar_ncms(ncms_extraidos, OUTPUT_FILE)

import os
print("Diretório de trabalho atual:", os.getcwd())