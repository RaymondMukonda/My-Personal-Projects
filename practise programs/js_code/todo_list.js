const todolist = ['make dinner', 'wash closthes'];

renderTodoList();

function renderTodoList() {
    let todolistHTML = '';

    for (let i = 0; i < todolist.length; i++) {
        const todo = todolist[i];
        const html = `
        <p>
            ${todo} <button onclick="
                todoList.splice(${i}, 1);
                renderTodoList();         
            ">Delete</button>
        <p>
        `;
        todolistHTML += html;
    }
    console.log(todolistHTML);

    document.querySelector('.js-todo-list')
    .innerHTML = todolistHTML;

}

function addTodo() {
    const inputElemnt  = document.querySelector('.js-name-input');
    const name = inputElemnt.value

    todolist.push(name);
    console.log(todolist);

    inputElemnt.value = '';

    renderTodoList();
};