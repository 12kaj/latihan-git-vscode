function showPassword() {
    var passwordInput = document.getElementById("password");
    var passwordType = passwordInput.type;

    if (passwordType === "password") {
      passwordInput.type = "text";
    } else {
      passwordInput.type = "password";
    }
  }

function auth() {
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
//condition

if (username === "aabbcc" && password === "112233") {
  window.location.assign("page.html");
  alert("Login successfully");
} else {
  alert("invalid information");
}
}