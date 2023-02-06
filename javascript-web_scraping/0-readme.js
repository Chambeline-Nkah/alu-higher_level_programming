#!/usr/bin/node
//Writing a script that reads and prints the content of a file
const fs = require('fs');
const file = process.argv.slice(2);

fs.readFile(file, (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
