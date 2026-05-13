import { greetUser } from "./arrow.js";

let me;
let you;

async function getData() {
  try {
    const response = await fetch('https://raw.githubusercontent.com/RaymondMukonda/My-Personal-Projects/refs/heads/main/API/data.json');
    const data = await response.json();

    me = data[0];
    you = data[1];
    

  } catch (error) {
    console.log('There has been an error: ',error)
  }
}


function greetStudents(user){
  console.log(`Hello ${user.name} we see that you current school with ${user.school} and started in ${user.year} `)
}


getData();

async function start() {
    await getData();

    console.log(me);
    console.log(you);

    greetStudents(me);
    greetStudents(you);

    const personOne = document.getElementById('btn1');
    const personTwo = document.getElementById('btn2');

    attachUserToButton(personOne, me);
    attachUserToButton(personTwo, you);

    
}

start();


// make reuseble code 
function attachUserToButton(button, user) {
  button.addEventListener('click', () => {
    button.innerHTML = `Name: ${user.name}<br>School: ${user.school}<br>Year: ${user.year}`;
  });
}


async function greetPeople () {
  await getData();
  greetUser(me);

}

greetPeople();




 