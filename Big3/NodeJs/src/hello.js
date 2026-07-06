import promptSync from 'prompt-sync';

const prompt = promptSync();

function greetUser() {
    let name = prompt('Hello Please enter your name: ');
    console.log(`What a beautiful name you have ${name}:`);
    let surname = prompt(`Please enter your surname Mr ${name}`);
    console.log(`Welcome to the club ${name} ${surname}`);
}

export {greetUser};

