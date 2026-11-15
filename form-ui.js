document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.header');
  if (header && !header.querySelector('.page-name')) {
    const pageName = document.createElement('span');
    pageName.className = 'page-name';
    pageName.textContent = document.title;
    header.appendChild(pageName);
  }

  document.querySelectorAll('.bloco').forEach((block) => {
    const heading = block.querySelector('h2');
    if (!heading) return;
    const title = heading.textContent.toLowerCase();
    if (!title.includes('ocorr') && !title.includes('infrig')) return;

    let button = block.querySelector('.copy-btn');
    if (!button) {
      button = document.createElement('button');
      button.type = 'button';
      button.className = 'copy-btn';
      heading.appendChild(button);
    }
    button.removeAttribute('onclick');
    button.textContent = 'Copiar';

    button.addEventListener('click', async () => {
      const content = block.cloneNode(true);
      content.querySelectorAll('h2, button').forEach((element) => element.remove());
      const text = content.innerText.trim();
      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const area = document.createElement('textarea');
        area.value = text;
        document.body.appendChild(area);
        area.select();
        document.execCommand('copy');
        area.remove();
      }
      button.textContent = 'Copiado ✓';
      window.setTimeout(() => { button.textContent = 'Copiar'; }, 1600);
    });
  });
});
