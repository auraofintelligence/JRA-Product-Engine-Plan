const menu=document.querySelector('.menu-toggle');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));document.querySelector('.nav').classList.toggle('open',open)});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menu){menu.setAttribute('aria-expanded','false');document.querySelector('.nav').classList.remove('open')}});
const topButton=document.querySelector('.top-btn');
function updateTop(){if(topButton)topButton.hidden=window.scrollY<450}
window.addEventListener('scroll',updateTop,{passive:true});updateTop();
topButton?.addEventListener('click',()=>{window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});document.querySelector('.brand').focus({preventScroll:true})});
if(matchMedia('(hover: hover) and (prefers-reduced-motion: no-preference)').matches){document.querySelectorAll('.card').forEach(card=>card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();card.style.setProperty('--x',`${e.clientX-r.left}px`);card.style.setProperty('--y',`${e.clientY-r.top}px`)}))}
