const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const ideas=require('../dist/assets/suggestions.js');
const html=fs.readFileSync(path.join(__dirname,'../dist/workbench.html'),'utf8');
const fields=new Set([...html.matchAll(/ name="([^"]+)"/g)].map(m=>m[1]));
const tabs=['brief','making','costs','offer','circular','connections','handoff'];
const presets=['aura-undies','aura-expressions','drinks','p4a','gajra','hygiene','purple-mat','sandy-club','joy-gathering'];
for(const preset of presets)for(const tab of tabs){
 const result=ideas.suggest({},preset,tab);
 assert.ok(result.groups.length,`${preset} missing context`);
 assert.ok(result.items.length>=2,`${preset}/${tab} missing ideas`);
 for(const item of result.items){assert.ok(fields.has(item.field)||item.field==='connection',item.field);assert.ok(item.text&&item.title);assert.ok(!/Cost$|^price$|^quantity$|^feePercent$|^permissionStatus$/.test(item.field),'Suggestions must not supply prices or permissions');}
}
assert.deepEqual(ideas.direction({name:'Lemon iced tea'},'aura-undies'),['drinks']);
assert.deepEqual(ideas.direction({name:'Purple bathroom mat'},'p4a'),['mat']);
assert.deepEqual(ideas.direction({name:'Dance leggings'}),['clothing']);
assert.deepEqual(ideas.direction({name:'A new idea',intention:'A drink for shared meals'}),['drinks']);
assert.deepEqual(ideas.direction({name:'Tea and shirts'}),['clothing','drinks']);
assert.deepEqual(ideas.direction({name:'Tea and shirts',ideasFocus:'objects'}),['objects']);
assert.ok(!ideas.suggest({name:'Lemon iced tea'},'aura-undies','making').items.some(x=>/garment|waistband/.test(x.text)));
assert.deepEqual(ideas.direction({name:'A unique new idea'}),[]);
assert.ok(ideas.suggest({name:'A unique new idea'},'','brief').items.length);
const text='My own existing notes.';
const combined=ideas.append(text,'Compare two samples.');
assert.equal(combined,'My own existing notes.\n\nCompare two samples.');
assert.equal(ideas.append(combined,'Compare two samples.'),combined);
const untouched={name:'Tea',intention:'My own idea'};ideas.suggest(untouched,'','offer');assert.deepEqual(untouched,{name:'Tea',intention:'My own idea'});
console.log('PASS: all nine presets across seven sections, changed ideas, mixed products, optional focus, unknown ideas, valid targets, no prices or permissions, preserving text and duplicate prevention');
