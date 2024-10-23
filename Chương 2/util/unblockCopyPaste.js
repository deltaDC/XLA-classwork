document.querySelectorAll('*').forEach(element => {
  element.oncopy = null;
  element.oncut = null;
  element.onpaste = null;
  element.oncontextmenu = null;
  element.onselectstart = null;
  element.ondragstart = null;
});

document.addEventListener('copy', (e) => e.stopPropagation(), true);
document.addEventListener('cut', (e) => e.stopPropagation(), true);
document.addEventListener('paste', (e) => e.stopPropagation(), true);
document.addEventListener('contextmenu', (e) => e.stopPropagation(), true);
document.addEventListener('selectstart', (e) => e.stopPropagation(), true);
document.addEventListener('dragstart', (e) => e.stopPropagation(), true);