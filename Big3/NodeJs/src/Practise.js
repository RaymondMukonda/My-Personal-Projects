const prompt = require('prompt-sync')();

let user = false;

while (!user) {
    const name = prompt('Kindly enter your name: ');
    const surname = prompt('Enter your surname please: ');

    // Check if inputs contain only letters
    const nameValid = /^[A-Za-z]+$/.test(name);
    const surnameValid = /^[A-Za-z]+$/.test(surname);

    if (!nameValid || !surnameValid) {
        console.log("Invalid input — please enter letters only!");
    } else {
        user = true;
        console.log(`Welcome, ${name} ${surname}!`);
    }
}
