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
let remotePointer=null;
let presenterPreview=null;
let presenterLaserButton=null;
const laserNamespace='hpc-laser';
const isPreview=new URLSearchParams(location.search).has('receiver');
const isCurrentPreview=isPreview&&window.frameElement?.parentElement.id==='current-slide';
const audienceWindow=isCurrentPreview?window.parent.opener:null;
function sendLaser(target,type,data={}){
  if(target&&!target.closed)target.postMessage(JSON.stringify({namespace:laserNamespace,type,...data}),location.origin);
}
function slideBounds(){return deck.getCurrentSlide()?.querySelector('.slide-inner').getBoundingClientRect();}
function sameSlide(position){
  const {h,v}=deck.getIndices();
  return position.h===h&&position.v===v;
}
function hideLaser(){laserPointer.hidden=true;}
function resetLaser(){
  pointerPosition=null;remotePointer=null;hideLaser();
  if(isCurrentPreview)sendLaser(audienceWindow,'hide');
}
function updateLaser(){
  if(!laserEnabled||document.hidden||contentDialog.open||deck.isOverview()||deck.isPaused()){
    hideLaser();return;
  }
  const bounds=slideBounds();
  if(!bounds?.width||!bounds.height){hideLaser();return;}
  let position=pointerPosition;
  if(remotePointer&&sameSlide(remotePointer)){
    position={x:bounds.left+remotePointer.x*bounds.width,y:bounds.top+remotePointer.y*bounds.height};
  }
  if(!position){hideLaser();return;}
  const {x,y}=position;
  const target=document.elementFromPoint(x,y);
  if(x<bounds.left||x>bounds.right||y<bounds.top||y>bounds.bottom||!target?.closest('.reveal')||target.closest('.controls')){
    hideLaser();return;
  }
  laserPointer.style.transform=`translate3d(${x}px,${y}px,0) translate(-50%,-50%)`;
  laserPointer.hidden=false;
}
function setLaserEnabled(enabled){
  laserEnabled=enabled;
  document.documentElement.classList.toggle('laser-enabled',laserEnabled);
  laserButton.setAttribute('aria-pressed',String(laserEnabled));
  laserButton.textContent=laserEnabled?'Laser on':'Laser';
  if(presenterLaserButton){
    presenterLaserButton.setAttribute('aria-pressed',String(laserEnabled));
    presenterLaserButton.textContent=laserEnabled?'Laser on (L)':'Laser (L)';
    presenterLaserButton.style.background=laserEnabled?'#7e2635':'#142b46';
  }
  if(!enabled)resetLaser();
  updateLaser();
}
function toggleLaser(){
  if(isCurrentPreview){sendLaser(audienceWindow,'toggle');return;}
  if(isPreview)return;
  setLaserEnabled(!laserEnabled);
  sendLaser(presenterPreview,'enabled',{enabled:laserEnabled});
}
function isPresenterPreview(source){
  try{
    return source&&source.parent!==source&&!source.parent.closed&&source.parent.opener===window&&
      source.parent.document.querySelector('#current-slide iframe')?.contentWindow===source&&
      source.location.pathname===location.pathname;
  }catch{return false;}
}
// The audience owns the on/off state. Only its speaker window's current
// preview may send coordinates; an upcoming preview or another tab cannot.
window.addEventListener('message',event=>{
  if(event.origin!==location.origin||typeof event.data!=='string')return;
  let data;
  try{data=JSON.parse(event.data);}catch{return;}
  if(data?.namespace!==laserNamespace)return;
  if(isCurrentPreview){
    if(event.source!==audienceWindow)return;
    if(data.type==='enabled'&&typeof data.enabled==='boolean'){
      const changed=laserEnabled!==data.enabled;
      setLaserEnabled(data.enabled);
      if(changed&&data.enabled)publishPointer();
    }
    return;
  }
  if(isPreview)return;
  if(!isPresenterPreview(event.source))return;
  presenterPreview=event.source;
  if(data.type==='hello')sendLaser(presenterPreview,'enabled',{enabled:laserEnabled});
  else if(data.type==='toggle')toggleLaser();
  else if(data.type==='hide'){remotePointer=null;updateLaser();}
  else if(data.type==='move'&&laserEnabled&&sameSlide(data)&&
    Number.isFinite(data.x)&&Number.isFinite(data.y)&&data.x>=0&&data.x<=1&&data.y>=0&&data.y<=1){
    pointerPosition=null;remotePointer=data;updateLaser();
  }
});
if(!isPreview)setInterval(()=>{
  // A closed popup can disappear before its final hide message is delivered.
  if(presenterPreview&&!isPresenterPreview(presenterPreview)){
    presenterPreview=null;remotePointer=null;updateLaser();
  }
},500);
function publishPointer(){
  if(!isCurrentPreview||!laserEnabled)return;
  const bounds=slideBounds();
  if(laserPointer.hidden||!bounds?.width){sendLaser(audienceWindow,'hide');return;}
  sendLaser(audienceWindow,'move',{
    x:(pointerPosition.x-bounds.left)/bounds.width,
    y:(pointerPosition.y-bounds.top)/bounds.height,
    h:deck.getIndices().h,v:deck.getIndices().v
  });
}
if(isCurrentPreview){
  const speaker=window.parent;
  // Reuse the speaker document without modifying the bundled Reveal plugin.
  speaker.hpcLaserCleanup?.();
  const controller=new speaker.AbortController();
  const options={signal:controller.signal};
  presenterLaserButton=speaker.document.createElement('button');
  presenterLaserButton.id='presenter-laser-btn';
  presenterLaserButton.type='button';
  presenterLaserButton.title='Point inside the current slide to show the laser on the audience display';
  presenterLaserButton.style.cssText='position:absolute;top:10px;left:10px;z-index:5;padding:8px 12px;border:0;border-radius:4px;color:white;font:14px Helvetica,sans-serif;cursor:pointer';
  presenterLaserButton.addEventListener('click',toggleLaser);
  speaker.document.querySelector('#current-slide').append(presenterLaserButton);
  setLaserEnabled(false);
  // Capture L before Reveal forwards it, preserving key-repeat behavior.
  speaker.document.addEventListener('keydown',event=>{
    if(event.code!=='KeyL'||event.ctrlKey||event.metaKey||event.altKey||event.target.closest('input,textarea,select,[contenteditable="true"]'))return;
    event.preventDefault();event.stopImmediatePropagation();
    if(!event.repeat)toggleLaser();
  },{...options,capture:true});
  speaker.addEventListener('blur',()=>{
    // Focusing the preview iframe also blurs its parent window.
    if(speaker.document.activeElement!==window.frameElement)resetLaser();
  },options);
  speaker.addEventListener('pagehide',resetLaser,options);
  speaker.document.addEventListener('visibilitychange',()=>{if(speaker.document.hidden)resetLaser();},options);
  const reconnect=setInterval(()=>sendLaser(audienceWindow,'hello'),1000);
  speaker.hpcLaserCleanup=()=>{controller.abort();clearInterval(reconnect);presenterLaserButton.remove();};
  window.addEventListener('pagehide',()=>{resetLaser();speaker.hpcLaserCleanup();},{once:true});
  deck.on('ready',()=>sendLaser(audienceWindow,'hello'));
}
laserButton.addEventListener('click',toggleLaser);
document.addEventListener('pointermove',event=>{
  if(event.pointerType==='touch')return;
  remotePointer=null;
  pointerPosition={x:event.clientX,y:event.clientY};
  updateLaser();
  publishPointer();
});
document.addEventListener('pointerout',event=>{
  if(!event.relatedTarget){pointerPosition=null;if(!remotePointer)hideLaser();if(isCurrentPreview)sendLaser(audienceWindow,'hide');}
});
document.addEventListener('pointercancel',resetLaser);
window.addEventListener('blur',()=>{pointerPosition=null;if(!remotePointer)resetLaser();});
window.addEventListener('resize',()=>{
  pointerPosition=null;
  if(isCurrentPreview)resetLaser();
  requestAnimationFrame(updateLaser);
});
document.addEventListener('visibilitychange',()=>{if(document.hidden)resetLaser();});
document.addEventListener('fullscreenchange',()=>{
  pointerPosition=null;
  const fullscreen=document.fullscreenElement;
  if(fullscreen&&!fullscreen.contains(laserPointer))fullscreen.append(laserPointer);
  else if(!fullscreen&&laserPointer.parentElement!==document.body)document.body.append(laserPointer);
  requestAnimationFrame(updateLaser);
});
deck.on('slidechanged',resetLaser);
deck.on('slidetransitionend',updateLaser);
deck.on('overviewshown',resetLaser);
deck.on('paused',resetLaser);
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
