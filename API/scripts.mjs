async function getData() {
  try {
    const response = await fetch('./data.json');
    const data = await response.json();

    const me = greetStudents(data[0]);
    const you = greetStudents(data[1]);
    

  } catch (error) {
    console.log('There has been an error: ',error)
  }
}


function greetStudents(user){
  console.log(`Hello ${user.name} we see that you current school with ${user.school} and started in ${user.year} `)
}

getData();



