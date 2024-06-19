#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i += 1) {
      if (c === undefined) { console.log('X'.repeat(this.width)); } else { console.log(c.repeat(this.width)); }
    }
  }
}
module.exports = Square;
