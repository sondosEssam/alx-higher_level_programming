#!/usr/bin/node
const square = require("./5-square.js");
class Square extends square {

  charPrint (c) {
    for (let i = 0; i < this.height; i += 1) {
      if (c === undefined) { console.log('X'.repeat(this.width)); } else { console.log(c.repeat(this.width)); }
    }
  }
}
module.exports = Square;
