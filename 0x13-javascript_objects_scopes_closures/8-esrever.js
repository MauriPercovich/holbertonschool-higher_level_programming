#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  const lastIndex = list.length - 1;

  for (let i = lastIndex; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return newArray;
};
