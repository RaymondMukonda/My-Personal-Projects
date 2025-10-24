function showForm(formId) {
  document.querySelectorAll(".form-box").forEach(form => {
    form.classList.remove("active");
  });
  document.getElementById(formId).classList.add("active");
}


// this will remember the page state on refresh
function showForm(formId) {
  document.querySelectorAll(".form-box").forEach(form => {
    form.classList.remove("active");
  });
  document.getElementById(formId).classList.add("active");

  // Save the active form ID
  localStorage.setItem("activeForm", formId);
}

//  Restore the state on page load
window.addEventListener("DOMContentLoaded", () => {
  const savedFormId = localStorage.getItem("activeForm");
  if (savedFormId) {
    document.querySelectorAll(".form-box").forEach(form => {
      form.classList.remove("active");
    });
    const targetForm = document.getElementById(savedFormId);
    if (targetForm) {
      targetForm.classList.add("active");
    }
  }
});

// // save input
document.querySelectorAll("input").forEach(input => {
  input.addEventListener("input", () => {
    localStorage.setItem(input.name, input.value);
  });
});

//  Restore on Page Load input
window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("input").forEach(input => {
    const savedValue = localStorage.getItem(input.name);
    if (savedValue !== null) {
      input.value = savedValue;
    }
  });
});