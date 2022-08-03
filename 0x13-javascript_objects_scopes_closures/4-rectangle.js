#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const rows = this.height;
    const columns = this.width;
    for (let i = 0; i < rows; i++) {
      console.log('X'.repeat(columns));
    }
  }

  rotate () {
    const pivot = this.width;
    this.width = this.height;
    this.height = pivot;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
