#!/usr/bin/node
exports.converter = function (base) {
  function numReturn (num) {
    return num.toString(base);
  }
  return (numReturn);
};
