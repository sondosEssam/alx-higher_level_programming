#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const args2 = args.sort();
  console.log(args2[args2.length - 2]);
}
