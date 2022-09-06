#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myArray = process.argv.slice(2);
  const bN = myArray.sort(function (a, b) { return a - b; });
  console.log(bN[bN.length - 2]);
}
