// const { createElement } = require("react");

const btn = document.getElementById('my-button');
const container = document.getElementById("container");

const div1 = document.createElement("div");
div1.textContent = "Using appendChild";
container.appendChild(div1); // only one node

const div2 = document.createElement("div");
div2.textContent = "Using append";
container.append("Extra text", div2); // text + node together






















































console.log();