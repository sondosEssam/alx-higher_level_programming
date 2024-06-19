#!/usr/bin/node
exports.esrever = function (list) {
  const count = [];
  for (let i = 0; i < list.length; i += 1) {
    count.push(list[list.length - i - 1]);
  }
  return count;
};
