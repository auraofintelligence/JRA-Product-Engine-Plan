const assert=require('node:assert/strict');
const fs=require('node:fs');
const journey=require('../dist/assets/journey.js');
const html=fs.readFileSync(require('node:path').join(__dirname,'../dist/workbench.html'),'utf8');
const fields=[...html.matchAll(/<(?:input|textarea|select)[^>]* name="([^"]+)"/g)].map(m=>m[1]);
assert.equal(fields.length,new Set(fields).size,'Moving fields must not create duplicate names');
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(ids.length,new Set(ids).size);
assert.equal(journey.steps.length,7);
assert.equal(journey.neighbour('brief',-1),null);
assert.equal(journey.neighbour('handoff',1),null);
assert.equal(journey.neighbour('making',1),'connections');
for(const step of journey.steps){
 assert.ok(html.includes(`id="panel-${step.key}"`));
 for(const key of [...step.fields,...step.context])assert.ok(fields.includes(key),`Lost field ${key}`);
}
assert.ok(journey.notes({}).every(n=>!n.started),'Blank drafts must not look complete');
assert.ok(journey.notes({materials:'Trial notes'}).find(n=>n.key==='making').started);
assert.ok(!journey.notes({price:'0'}).find(n=>n.key==='brief').started);
assert.ok(journey.notes({},[{name:'Possible maker'}]).find(n=>n.key==='connections').started);
// Every old backup field remains available after restructuring.
const previous=['name','audience','intention','expressions','specification','ideasFocus','materials','sampleVersion','maker','feedback','contributors','materialsCost','labourCost','packagingCost','freightCost','otherCost','price','fixedCost','feePercent','quantity','costNotes','offer','salesRoute','fulfilment','terms','marketing','creative','community','participation','care','receiver','sent','returned','unit','nextUse','agentTask','permissions','limits','reviewer','questions','permissionStatus'];
assert.deepEqual([...fields].sort(),previous.sort());
console.log('PASS: journey order, boundaries, honest draft indicators, unique fields and all previous backup fields retained');
