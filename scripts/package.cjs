/* Allowlist-only static package. Never copies PDFs, source reports or Git history. */
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),out=path.join(root,'dist');
const html=['index.html','es.html','sr.html','quiz.html','games.html'];
const files=new Set([...html,'css/tailwind.css','css/center.css','css/presentation.css','css/TAILWIND-LICENSE.txt','js/i18n.js','js/core.js','js/knowledge.js','js/presentation.js','js/practice.js','js/vendor/alpine-3.15.8.min.js','js/vendor/LICENSE.txt']);
for(const name of html)for(const match of fs.readFileSync(path.join(root,name),'utf8').matchAll(/src="(assets\/[^"?#]+\.png)"/g))files.add(match[1]);
function walk(dir){return fs.existsSync(dir)?fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]):[];}
for(const file of walk(out)){const relative=path.relative(out,file).split(path.sep).join('/');if(!files.has(relative)&&!['.nojekyll','manifest.json'].includes(relative))throw Error('Unexpected file in dist; inspect before packaging: '+relative);}
const manifest=[];for(const file of [...files].sort()){if(file.includes('..')||path.isAbsolute(file))throw Error('Unsafe path');const source=path.join(root,file),target=path.join(out,file);fs.mkdirSync(path.dirname(target),{recursive:true});fs.copyFileSync(source,target);const data=fs.readFileSync(target);manifest.push({file,bytes:data.length,sha256:crypto.createHash('sha256').update(data).digest('hex')});}
fs.writeFileSync(path.join(out,'.nojekyll'),'');fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify({generated:new Date().toISOString(),files:manifest},null,2));console.log(`Packaged ${files.size} reviewed application files in dist. No deployment performed.`);
