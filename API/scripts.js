function greetUser(user) {
    console.log(`hello user from feteched data ${user.name}`)
}

async function getData() {
    try {

        const response = await fetch('data.json');
        const userData = await response.json();

        greetUser(userData);

        console.log('Data fetched', userData);
        console.log('name: ', userData.name);
        console.log('school: ', userData.school);
        console.log('year: ', userData.year);


    } catch(error) {
        console.log('the was an error: ', error)
    }
}

getData();

