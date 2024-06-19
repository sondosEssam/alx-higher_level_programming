#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
if (isNaN((Number(firstArg)))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i += 1) {
    console.log('C is fun');
  }
}
