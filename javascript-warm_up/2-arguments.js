#!/usr/bin/node
const args = process.argv[2];
switch (args) {
  case 0:
    console.log('No arguments');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
