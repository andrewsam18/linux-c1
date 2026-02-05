document.addEventListener("DOMContentLoaded", function () {
  var navLinks = document.getElementById("navLinks");
  var openBtn = document.getElementById("showMenu");
  var closeBtn = document.getElementById("hideMenu");

  openBtn.addEventListener("click", function () {
    navLinks.style.right = "0";
  });

  closeBtn.addEventListener("click", function () {
    navLinks.style.right = "-200px";
  });
});
id="showMenu" 
id="hideMenu"