const findVowels = function (str) {
  let vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"];
  let vowelCounter = 0;
  for (let i = 0; i < str.length; i++) {
    if (vowels.indexOf(str[i]) >= 0) {
      vowelCounter += 1;
    }
  }
  return vowelCounter;
};
console.log(findVowels("dg"));
