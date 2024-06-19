#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const args2 = args.map(Number);
  const args3 = args2.sort((a, b) => a - b);
  console.log(args3[args3.length - 2]);
}
