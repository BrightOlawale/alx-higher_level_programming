#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || !width || !height) {
      return;
    }
    this.width = width;
    this.height = height;
  }
};
