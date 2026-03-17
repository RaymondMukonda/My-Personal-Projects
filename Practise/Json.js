const person = {
  name: "Raymond",
  age: 25
};

const jsonPerson = `{
  "name": "Raymond",
  "age": 25
}`;

const javaToJson = JSON.stringify(person);

console.log(javaToJson);


const jsonToJava = JSON.parse(jsonPerson);
console.log(person); 
// Raymond
