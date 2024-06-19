#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
if (isNaN((Number(firstArg)))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(firstArg); i += 1) {
    console.log('X'.repeat((Number(firstArg))));
  }
}
