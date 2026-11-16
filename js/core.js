(() => {
'use strict';
const shuffle=(items,rng=Math.random)=>{const a=[...items];for(let i=a.length-1;i>0;i--){const j=Math.floor(rng()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
const selectQuiz=(questions,count=20,rng=Math.random)=>{if(questions.length<count)throw Error('Insufficient questions');const groups=new Map();for(const q of questions){if(!groups.has(q.topic))groups.set(q.topic,[]);groups.get(q.topic).push(q);}const buckets=shuffle([...groups.values()].map(g=>shuffle(g,rng)),rng),out=[];while(out.length<count){for(const b of buckets){if(b.length&&out.length<count)out.push(b.pop());}}return shuffle(out,rng).map(q=>({...q,options:shuffle(q.options,rng)}));};
const isCorrect=(item,id)=>item.answer===id;
const scorePercent=(correct,total)=>total?Math.round(correct/total*100):0;
globalThis.SAC_CORE={shuffle,selectQuiz,isCorrect,scorePercent};
if(typeof module!=='undefined')module.exports=globalThis.SAC_CORE;
})();
