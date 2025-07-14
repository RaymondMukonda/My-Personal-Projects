const todolist = [];

function addTodo() {
    const inputElemnt  = document.querySelector('.js-name-input');
    const name = inputElemnt.value

    todolist.push(name);
    console.log(todolist);

    inputElemnt.value = '';
};