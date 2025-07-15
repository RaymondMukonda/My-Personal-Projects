const todoList = [{
    name: 'make dinner',
    dueDate: '2025-07-12'
}, {
    name: 'make pap',
    dueDate: '2025-07-12'
}];

renderTodoList();

function renderTodoList() {
    let todoListHTML = '';

    for (let i = 0; i < todoList.length; i++) {
        const todoObject = todoList[i];
        const { name, dueDate } = todoObject;
        // const name = todoObject.name; same as above code
        // const dueDate = todoObject.dueDate;
        const html = `
        <div>${name}</div>
        <div>${dueDate}</div>

        <button onclick="
        todoList.splice(${i}, 1);
        renderTodoList();         
        " class="delete-todo-button" >Delete</button>

        `;
        todoListHTML += html;
    }

    document.querySelector('.js-todo-list')
    .innerHTML = todoListHTML;

}

function addTodo() {
    const inputElemnt  = document.querySelector('.js-name-input');
    const name = inputElemnt.value;

    const dateInputElement = document.querySelector('.js-due-date-input');
    const dueDate = dateInputElement.value;

    todoList.push({
        // name: name,
        // duedate: dueDate same as below
        name,
        dueDate
    });

    inputElemnt.value = '';

    renderTodoList();
};