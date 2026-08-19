import promptSync from 'prompt-sync';

const prompt = promptSync();

function greetUser() {
    let name = prompt("Hi please enter your name: ");
    console.log(`What a beautiful name you have ${name}`)
    let age = prompt("now could you kindly tell me you age: ");

    if (age >= 18) {
        console.log(`Hi ${name} we have checked your age and we can see you are well over 18 seeing as you placed ${age} in our database`);
    } else {
        console.log(`Hi ${name} you are currently under age`)
    }
}

export {greetUser};

