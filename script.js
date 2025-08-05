function solicitarNF() {
    let notaFiscal = prompt("Digite o número da NF:");
    if (notaFiscal !== null && notaFiscal !== "") {
        let elementoTexto = document.getElementById("nf");
        elementoTexto.innerHTML = elementoTexto.innerHTML.replace("[NF]", notaFiscal);
    } else {
        alert("Você não inseriu um número!");
    }

}

window.onload = solicitarNF;

function solicitarVM() {
    let valorMercadoria = prompt("Digite o valor da mercadoria:");
    if (valorMercadoria !== null && valorMercadoria !== "") {
        let elementoMercadoria = document.getElementById("VM");
        elementoMercadoria.innerHTML = elementoMercadia.innerHTML.replace("[30.125,25]", valorMercadoria);
    } else {
        alert("Você não inseriu um valor!");
    }

}

window.onload = solicitarVM;