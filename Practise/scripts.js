const userInput = require('prompt-sync')();

let name1 = userInput('please enter the first name: ');
let name2 = userInput('please enter the second name: ');


class Person {
  constructor(name) {
    this.name = name;
  }
  talk() {
    return `${this.name} is talking`;
  }
}

const me = new Person(name1);
const you = new Person(name2);



console.log(`hello ${me.name} and ${you.name} im honred to meet you both`);