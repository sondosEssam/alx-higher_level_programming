#!/usr/bin/node
const args = process.argv.slice(2);

const firstArg = args[0];
if (!isNaN(firstArg)) {
  console.log('My number: ' + Number(firstArg));
} else {
  console.log('Not a number');
}
