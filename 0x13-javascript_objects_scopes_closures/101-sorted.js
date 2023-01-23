#!/usr/bin/node

imported = require('./101-data.js').dict;
const dictN = {};
for (const [key, value] in Object.entries(imported)) {
  dictN[value].push(key);
}

console.log(dictN);
    