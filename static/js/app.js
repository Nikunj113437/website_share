const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


document.getElementById('signup_form').addEventListener('submit', function (event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  const request = new XMLHttpRequest();
  request.open('POST', form.action);
  request.responseType = 'json';
  request.send(formData);
  request.onload = function () {
    if (request.status === 200) {
      const message = request.response.message;
      // alert(message);
      form.reset();
      if (message == "Signup Successful!") {
        window.location.href = 'http://16.171.166.55/after_login/';
      }
    } else {
      alert('An error occurred. Please try again.');
    }
  };
});


document.getElementById('login_form').addEventListener('submit', function (event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  const request = new XMLHttpRequest();
  request.open('POST', form.action);
  request.responseType = 'json';
  request.send(formData);
  request.onload = function () {
    if (request.status === 200) {
      const message = request.response.message;
      // alert(message);
      form.reset();
      if (message == "Login successful!") {
        window.location.href = 'http://16.171.166.55/after_login/';
      }
    } else {
      alert('An error occurred. Please try again.');
    }
  };
});