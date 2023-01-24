module.exports.add = (a, b) => a + b;
module.exports.subtract = (a, b) => a - b;

const mathUtilities = require("./mathUtilities");
console.log(mathUtilities.add(1, 2));
console.log(mathUtilities.subtract(5, 2));
