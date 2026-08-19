import { greetUser } from "./hello.js";
import { promises as fs } from 'fs';

// greetUser();

// class Person {
//     talk() {
//         return 'you are talking'
//     }
// }

// class fly extends Person {
//     flyUp() {
//         return 'the person from talking is flying up '
//     }
// }

// const me = new fly;
// console.log(me.flyUp());
// console.log(me.talk());

async function getdata() {
    try {
        const file = await fs.readFile('./data.json', 'utf-8');
        const data = JSON.parse(file);

        console.log(`hello ${JSON.stringify(data)}`);
    } catch (err) {
        console.log(`There has been an error found: ${err}`);
    }
}

getdata();