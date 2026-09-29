

function orderPizaa(callback) {
    setTimeout(() => {
        const pizza = '🍕';
        callback(pizza)
    }, 2000)
}

function pizzaReady(pizza) {
    console.log(`Eat the ${pizza}`);
}

orderPizaa(pizzaReady);
console.log('Call qoul');

console.log('Call qoul');

// function changed() {
//     const button = document.getElementById('callme');
//     button.addEventListener('click', () => {
//         setTimeout(() => {
//             button.innerHTML = 'Ive been clicked';
//         }, 2000);
//     });
// }


// changed();

const button = document.getElementById('callme');
button.addEventListener('click', () => {
    setTimeout(() => {
        button.innerHTML = "I've been clicked";
    }, 2000);
}); 