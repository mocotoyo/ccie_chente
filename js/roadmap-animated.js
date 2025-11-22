const panelContent = document.getElementById('panelContent');
const blocks = document.querySelectorAll('.block');
const progressFill = document.querySelector('.progress-fill');
const svg = document.getElementById('svgPaths');
const langSelect = document.getElementById('lang');

let paths = [];

// Helper to get content by language preference
function getContent(block, lang) {
  if(lang === 'en') return block.dataset.contentEn || block.dataset.content;
  if(lang === 'es') return block.dataset.contentEs || block.dataset.content;
  // both: show both concatenated
  const en = block.dataset.contentEn || block.dataset.content;
  const es = block.dataset.contentEs || block.dataset.content;
  return en + "<hr>" + es;
}

// Create paths between blocks (positions may change after load/resizes)
function createPaths() {
  // clear existing
  while(svg.firstChild) svg.removeChild(svg.firstChild);
  // re-add defs (marker)
  const defs = document.createElementNS("http://www.w3.org/2000/svg","defs");
  defs.innerHTML = '<marker id="arrowhead" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto"><polygon points="0 0,10 3,0 6" fill="#333"/></marker>';
  svg.appendChild(defs);

  paths = [];
  blocks.forEach((block,i)=>{
    if(i<blocks.length-1){
      const nextBlock = blocks[i+1];
      const rect1 = block.getBoundingClientRect();
      const rect2 = nextBlock.getBoundingClientRect();
      // compute y positions relative to the document (add scrollY)
      const y1 = rect1.top + rect1.height/2 + window.scrollY;
      const y2 = rect2.top + rect2.height/2 + window.scrollY;
      const svgX = Math.round(window.innerWidth * 0.35); // position curves roughly
      const path = document.createElementNS("http://www.w3.org/2000/svg","path");
      path.setAttribute("d",`M${svgX},${y1} C${svgX+60},${y1+80} ${svgX+60},${y2-80} ${svgX},${y2}`);
      path.setAttribute("stroke","#333");
      path.setAttribute("stroke-width","3");
      path.setAttribute("fill","none");
      path.setAttribute("marker-end","url(#arrowhead)");
      // progressive drawing
      const len = path.getTotalLength();
      path.style.strokeDasharray = len;
      path.style.strokeDashoffset = len;
      svg.appendChild(path);
      paths.push({path,len,start:y1,end:y2});
    }
  });
}

function updatePanelAndProgress() {
  let currentBlock = blocks[0];
  blocks.forEach(block=>{
    const rect = block.getBoundingClientRect();
    if(rect.top < window.innerHeight/2){
      currentBlock = block;
    }
  });
  const lang = langSelect.value;
  panelContent.innerHTML = getContent(currentBlock, lang);

  const scrollTop = window.scrollY;
  const docHeight = document.body.scrollHeight - window.innerHeight;
  const scrollPercent = docHeight>0 ? (scrollTop/docHeight)*100 : 0;
  progressFill.style.height = scrollPercent + '%';

  // animate paths based on scroll position
  paths.forEach(p=>{
    // compute how far along the path should be drawn
    const centerView = scrollTop + window.innerHeight/2;
    const t = Math.min(Math.max((centerView - p.start) / (p.end - p.start), 0), 1);
    p.path.style.strokeDashoffset = p.len * (1 - t);
  });
}

// initial creation after load
window.addEventListener('load', ()=>{
  createPaths();
  updatePanelAndProgress();
  // set initial panel language content
  panelContent.innerHTML = getContent(blocks[0], langSelect.value);
});

// recalc on resize and after fonts load
window.addEventListener('resize', ()=>{
  createPaths();
  updatePanelAndProgress();
});
window.addEventListener('scroll', updatePanelAndProgress);
langSelect.addEventListener('change', updatePanelAndProgress);

// re-create paths after a short timeout to account for layout shifts
setTimeout(()=>{ createPaths(); updatePanelAndProgress(); }, 500);
