'use strict';
const ids=['title','date','category','excerpt','body'];
const fields=Object.fromEntries(ids.map(id=>[id,document.getElementById(id)]));
const key='giovanni-field-note-v1';
const status=document.getElementById('saved');
fields.date.value=new Date(Date.now()-new Date().getTimezoneOffset()*60000).toISOString().slice(0,10);
try {const saved=JSON.parse(localStorage.getItem(key)||'null');if(saved)ids.forEach(id=>{if(typeof saved[id]==='string')fields[id].value=saved[id]});}catch{}
function render(){
 document.getElementById('preview-title').textContent=fields.title.value||'Untitled field note';
 document.getElementById('preview-meta').textContent=fields.category.value+' / '+fields.date.value;
 document.getElementById('preview-excerpt').textContent=fields.excerpt.value;
 const container=document.getElementById('preview-body');container.replaceChildren();
 let code=null,list=null;
 for(const block of fields.body.value.split('\n')){
  if(block.startsWith('```')){if(code){code=null;}else{const pre=document.createElement('pre');code=document.createElement('code');pre.append(code);container.append(pre);}list=null;continue;}
  if(code){code.textContent+=block+'\n';continue;}
  if(block.startsWith('- ')){if(!list){list=document.createElement('ul');container.append(list);}const li=document.createElement('li');li.textContent=block.slice(2);list.append(li);continue;}
  list=null;if(!block.trim())continue;
  const heading=block.startsWith('## ');const el=document.createElement(heading?'h2':'p');el.textContent=heading?block.slice(3):block;container.append(el);
 }
}
function update(){render();try{localStorage.setItem(key,JSON.stringify(Object.fromEntries(ids.map(id=>[id,fields[id].value]))));status.textContent='Draft saved in this browser.';}catch{status.textContent='Browser storage unavailable. Export your draft to keep it.';}}
ids.forEach(id=>fields[id].addEventListener('input',update));
document.getElementById('editor').addEventListener('submit',event=>{
 event.preventDefault();
 const clean=value=>value.replace(/[\r\n]+/g,' ').trim();
 const title=clean(fields.title.value);
 const slug=title.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'field-note';
 const markdown=`---\ntitle: ${title}\ndate: ${fields.date.value}\ncategory: ${clean(fields.category.value)}\nexcerpt: ${clean(fields.excerpt.value)}\ndraft: true\n---\n\n${fields.body.value}\n`;
 const url=URL.createObjectURL(new Blob([markdown],{type:'text/markdown;charset=utf-8'}));
 const link=document.createElement('a');link.href=url;link.download=slug+'.md';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);status.textContent='Draft exported. Add it to the site collection to publish.';
});
document.getElementById('clear').addEventListener('click',()=>{if(!confirm('Clear the draft stored in this browser? Export it first if you want to keep it.'))return;for(const id of ['title','excerpt','body'])fields[id].value='';update();});
render();
