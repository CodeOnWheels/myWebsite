'use strict';
(() => {
 const buttons = [...document.querySelectorAll('[data-bio-language]')];
 const panels = {en: document.getElementById('bio-en'), 'zh-Hant': document.getElementById('bio-zh')};
 function select(language, persist) {
  if (!Object.hasOwn(panels, language)) return;
  for (const [code, panel] of Object.entries(panels)) panel.hidden = code !== language;
  for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.bioLanguage === language));
  if (persist) {try {localStorage.setItem('giovanni-bio-language', language);} catch {}}
 }
 for (const button of buttons) button.addEventListener('click', () => select(button.dataset.bioLanguage, true));
 try {select(localStorage.getItem('giovanni-bio-language'), false);} catch {}
})();
