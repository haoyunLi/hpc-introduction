const deck = new Reveal({
  width:1440, height:810, margin:0.035, minScale:0.1, maxScale:2,
  hash:true, history:true, center:false, controls:true,
  controlsBackArrows:'visible', controlsTutorial:false,
  navigationMode:'default', progress:true, transition:'slide',
  transitionSpeed:'fast', backgroundTransition:'none', overview:true,
  slideNumber:false, pdfSeparateFragments:false, pdfMaxPagesPerSlide:1,
  plugins:[RevealNotes]
});
window.deck=deck;
const leafSlides=[...document.querySelectorAll('.slides .lecture-slide')];
const contentDialog=document.querySelector('#contents');
const notesPanel=document.querySelector('#notes-panel');
const laserButton=document.querySelector('#laser-btn');
const laserPointer=document.createElement('div');
laserPointer.id='laser-pointer';
laserPointer.setAttribute('aria-hidden','true');
laserPointer.hidden=true;
document.body.append(laserPointer);
let laserEnabled=false;
let pointerPosition=null;
function hideLaser(){laserPointer.hidden=true;}
function resetLaser(){pointerPosition=null;hideLaser();}
function updateLaser(){
  if(!laserEnabled||!pointerPosition||document.hidden||contentDialog.open||deck.isOverview()){
    hideLaser();return;
  }
  const {x,y}=pointerPosition;
  const target=document.elementFromPoint(x,y);
  if(!target?.closest('.reveal')||target.closest('.controls')){
    hideLaser();return;
  }
  laserPointer.style.transform=`translate3d(${x}px,${y}px,0) translate(-50%,-50%)`;
  laserPointer.hidden=false;
}
function toggleLaser(){
  laserEnabled=!laserEnabled;
  document.documentElement.classList.toggle('laser-enabled',laserEnabled);
  laserButton.setAttribute('aria-pressed',String(laserEnabled));
  laserButton.textContent=laserEnabled?'Laser on':'Laser';
  updateLaser();
}
laserButton.addEventListener('click',toggleLaser);
document.addEventListener('pointermove',event=>{
  if(event.pointerType==='touch')return;
  pointerPosition={x:event.clientX,y:event.clientY};
  updateLaser();
});
document.addEventListener('pointerout',event=>{
  if(!event.relatedTarget){pointerPosition=null;hideLaser();}
});
document.addEventListener('pointercancel',()=>{pointerPosition=null;hideLaser();});
window.addEventListener('blur',()=>{pointerPosition=null;hideLaser();});
window.addEventListener('resize',resetLaser);
document.addEventListener('visibilitychange',()=>{if(document.hidden){pointerPosition=null;hideLaser();}});
document.addEventListener('fullscreenchange',()=>{
  resetLaser();
  const fullscreen=document.fullscreenElement;
  if(fullscreen&&!fullscreen.contains(laserPointer))fullscreen.append(laserPointer);
  else if(!fullscreen&&laserPointer.parentElement!==document.body)document.body.append(laserPointer);
});
function syncNotes(){
  const slide=deck.getCurrentSlide();
  if(!slide?.matches('.lecture-slide'))return;
  document.querySelector('#note-content').innerHTML=`<h2>${slide.dataset.title}</h2>`+slide.querySelector('aside.notes').innerHTML;
  const {h,v}=deck.getIndices();
  document.querySelector('#position-label').textContent=`${slide.dataset.section} · ${h+1}.${v+1} · ${Number(slide.dataset.index)+1}/${leafSlides.length}`;
}
function toggleNotes(){
  notesPanel.hidden=!notesPanel.hidden;
  syncNotes();
  notesPanel.hidden?updateLaser():resetLaser();
}
function toggleContents(){
  if(contentDialog.open){contentDialog.close();updateLaser();}
  else{contentDialog.showModal();resetLaser();}
}
document.querySelector('#notes-btn').addEventListener('click',toggleNotes);
document.querySelector('#close-notes').addEventListener('click',()=>notesPanel.hidden=true);
document.querySelector('#contents-btn').addEventListener('click',toggleContents);
document.querySelector('.close-dialog').addEventListener('click',()=>contentDialog.close());
document.querySelector('#fullscreen-btn').addEventListener('click',()=>{
  if(document.fullscreenElement)document.exitFullscreen();
  else document.documentElement.requestFullscreen?.();
});
document.querySelectorAll('.slides > .chapter-stack').forEach((stack,h)=>{
  const group=document.createElement('div');group.className='contents-chapter';
  const title=document.createElement('h3');title.textContent=`${h+1}. ${stack.dataset.chapter}`;group.append(title);
  [...stack.children].filter(s=>s.matches('.lecture-slide')).forEach((slide,v)=>{
    const button=document.createElement('button');
    button.dataset.h=h;button.dataset.v=v;
    const index=document.createElement('span');index.className='idx';index.textContent=`${h+1}.${v+1}`;
    button.append(index,document.createTextNode(slide.dataset.title));
    button.addEventListener('click',()=>{deck.slide(h,v);contentDialog.close();});
    group.append(button);
  });
  document.querySelector('#contents-list').append(group);
});
document.querySelectorAll('[data-go-chapter]').forEach(button=>button.addEventListener('click',()=>deck.slide(Number(button.dataset.goChapter),0)));
document.querySelectorAll('.code-line').forEach(button=>button.addEventListener('click',()=>{
  const block=button.closest('.annotated');
  block.querySelectorAll('.code-line').forEach(b=>b.classList.remove('active'));
  button.classList.add('active');
  block.querySelector('.line-explanation').textContent=button.dataset.explain;
}));
deck.addKeyBinding({keyCode:78,key:'N',description:'Show in-window speaker notes'},toggleNotes);
deck.addKeyBinding({keyCode:67,key:'C',description:'Open course contents'},toggleContents);
deck.addKeyBinding({keyCode:76,key:'L',description:'Toggle laser pointer'},event=>{
  if(!event.repeat)toggleLaser();
});
deck.on('overviewshown',hideLaser);
deck.on('overviewhidden',updateLaser);
function fitCode(slide){
  if(!slide)return;
  slide.querySelectorAll('pre').forEach(pre=>{
    pre.style.fontSize='';const code=pre.querySelector('code');if(!code)return;
    const style=getComputedStyle(pre);
    const available=pre.clientWidth-parseFloat(style.paddingLeft)-parseFloat(style.paddingRight);
    if(available<=0)return;
    const context=document.createElement('canvas').getContext('2d');
    const size=parseFloat(style.fontSize);context.font=`${size}px ${getComputedStyle(code).fontFamily}`;
    const longest=Math.max(...code.textContent.split('\n').map(line=>context.measureText(line).width));
    if(longest>available)pre.style.fontSize=`${Math.max(20,size*available/longest)}px`;
  });
}
deck.on('ready',()=>{syncNotes();fitCode(deck.getCurrentSlide());});
deck.on('slidechanged',()=>{syncNotes();fitCode(deck.getCurrentSlide());});
deck.initialize().then(()=>{syncNotes();fitCode(deck.getCurrentSlide());window.presentationReady=true;});
