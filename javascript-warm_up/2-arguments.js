#!/usr/bin/node
const args=process.argv.length;
switch (args){
    case 2:
        console.log("No arguments");
        break;
    case 3:
        console.log("Arument found");
        break;
    default:
        console.log("Arguments found");
        break;
}
