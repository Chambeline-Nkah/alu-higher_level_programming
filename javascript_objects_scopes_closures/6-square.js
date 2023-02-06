module.exports = class Square extends require ('./5-square') {
  CharPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
    }
  }
};
