async function getData() {
  try {
    const response = await fetch("https://raw.githubusercontent.com/RaymondMukonda/My-Personal-Projects/main/API/data.json");
    const students = await response.json();
    console.log(students);

    const me = greetUser(students[0]);
    const you = greetUser(students[1]);

  } catch (error) {
    console.error("There was an error:", error);
  }
}

getData();


function greetUser(student) {
  console.log(`Hello ${student.name} from ${student.school}, year ${student.year}`);
}





