#!/usr/bin/node
const nm = parseInt(process.argv[2]);
if (nm) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
    console.log('Missing number of occurences');
}
