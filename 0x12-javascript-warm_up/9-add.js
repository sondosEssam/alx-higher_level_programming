#!/usr/bin/node
const args = process.argv.slice(2);

const firstArg = args[0];
const secondArg = args[1];
function add (a, b) {
  console.log(Number(firstArg) + Number(secondArg));
}
add(firstArg, secondArg);
