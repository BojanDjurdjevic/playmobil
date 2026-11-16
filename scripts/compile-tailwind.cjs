/* Optional maintainer tool: node scripts/compile-tailwind.cjs /path/to/tailwindcss
   The generated CSS is committed. Running the application needs no build or npm. */
const fs=require('node:fs'),path=require('node:path');
const root=process.argv[2];if(!root)throw Error('Pass an installed Tailwind CSS 4 package directory.');
const tw=require(path.join(root,'dist','lib.js'));
(async()=>{const input='@layer theme, base, components, utilities;\n@layer theme {\n'+fs.readFileSync(path.join(root,'theme.css'),'utf8')+'\n}\n@layer base {\n'+fs.readFileSync(path.join(root,'preflight.css'),'utf8')+'\n}\n@tailwind utilities;';
const classes=new Set();for(const file of ['index.html','es.html','sr.html']){const html=fs.readFileSync(file,'utf8');for(const match of html.matchAll(/class="([^"]+)"/g))for(const c of match[1].split(/\s+/))classes.add(c);}
const compiler=await tw.compile(input);fs.writeFileSync('css/tailwind.css',compiler.build([...classes]));console.log('Compiled',classes.size,'Tailwind classes.');})();
