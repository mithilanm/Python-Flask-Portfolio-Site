function myFunction() {
  var x = document.getElementById("Topnav");
  if (x.className == "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

var btnContainer = document.getElementById("topnav");
var btns = btnContainer.getElementsByClassName("btn");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }
    this.className += " active";
  });
}
