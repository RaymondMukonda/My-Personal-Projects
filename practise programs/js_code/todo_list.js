const todolist = ['Make dineer', 'wash dishes'];

let todolistHTML = '';

for (let i = 0; i < todolist.length; i++) {
    const todo = todolist[i];
    const html = `<p>${todo}<p>`;
    todolistHTML += html;
}; 




function addTodo() {
    const inputElemnt  = document.querySelector('.js-name-input');
    const name = inputElemnt.value

    todolist.push(name);
    console.log(todolist);

    inputElemnt.value = '';
};