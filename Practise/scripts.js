const prompt = require("prompt-sync")();

let country = 'south africa';
let ageDrive = 18;
let userName = '';
let usersurName = '';

let user = prompt('Please enter your country of origin: ');
userName = prompt('Please enter your name: ');
usersurName = prompt('Please enter your  surname: ');

if (user == country) {
  console.log(`Hi the ${userName} ${usersurName}  fellow south african !!`);
  let userAge = Number(prompt('Please enter your age: '));

  if (userAge >= 18)
  {
    console.log('you are well over age to drive');
  } else {
    console.log('you are still young to drive');
  }

} else {
  console.log('sorry you not south african');
}