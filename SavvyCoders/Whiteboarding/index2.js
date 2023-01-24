const vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"];
function findVowels(string) {
  let found = string.filter(vowels);
  console.log(found.length);
}
findVowels("Savvy Coders");
