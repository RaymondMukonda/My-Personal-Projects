const prompt = require("prompt-sync")();

let age = Number(prompt("Enter your age: "));

let votable;
if (Number.isNaN(age)) {
  votable = "input is not a number";
} else {
  votable = (age < 18) ? "too young" : "old enough";
}

console.log(votable);