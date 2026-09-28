/* A suggested route through one record, never a completion or approval score. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.JRAJourney=api;})(typeof globalThis!=='undefined'?globalThis:this,()=>{
const steps=[
 {key:'brief',label:'Your idea',title:'Start with the experience.',lead:'Who is this for, and what would make it useful or enjoyable? A few sentences are enough to begin.',next:'Take this idea into a first sample.',fields:['name','intention','audience'],context:[]},
 {key:'making',label:'First sample',title:'Give the idea a shape.',lead:'Choose what to try first. Keep the sample small enough to learn from, then add detail as you discover it.',next:'Now consider who could help make it happen.',fields:['materials','sampleVersion','feedback'],context:['intention','specification']},
 {key:'connections',label:'People & means',title:'Connect the people and skills.',lead:'Use the sample plan to explore makers, materials and contributions. A possible connection can start as a question.',next:'Bring those materials and conversations into the estimate.',fields:['maker','contributors'],context:['materials','sampleVersion']},
 {key:'costs',label:'The numbers',title:'Find a workable starting price.',lead:'Use the chosen sample and actual quotes. Unknowns can stay blank while you keep shaping the idea.',next:'Use what you know to describe a clear offer.',fields:['materialsCost','labourCost','price','costNotes'],context:['materials','maker']},
 {key:'offer',label:'The offer',title:'Make the invitation clear.',lead:'Turn the brief, sample and estimate into something another person can understand: what they receive and how it reaches them.',next:'Think beyond the handover to care, feedback and next use.',fields:['offer','fulfilment','marketing'],context:['audience','specification','price']},
 {key:'circular',label:'Life & next use',title:'Keep the good things going.',lead:'Connect the offer to everyday care, people’s experience and a useful next life. Add measured results when a real trial happens.',next:'Bring the whole idea together and choose your next move.',fields:['care','community','receiver'],context:['offer','materials']},
 {key:'handoff',label:'Bring it together',title:'See the whole idea.',lead:'Read the connected draft, return to anything you want to change, then save or download it. You can keep exploring with gaps still open.',next:'Take this draft into a conversation or another round of making.',fields:['agentTask','questions'],context:[]}
];
function notes(fields,links=[]){return steps.map(step=>({key:step.key,label:step.label,started:step.key==='connections'?links.length>0||step.fields.some(k=>String(fields[k]||'').trim()):step.fields.some(k=>String(fields[k]||'').trim())}));}
function neighbour(key,offset){const i=steps.findIndex(s=>s.key===key);return steps[i+offset]?.key||null;}
return {steps,notes,neighbour};
});
