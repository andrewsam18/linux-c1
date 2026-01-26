document.addEventListener("DOMContentLoaded", function () {
  // ----- Menu Toggle -----
  var MenuItems = document.getElementById("MenuItems");
  if (MenuItems) MenuItems.style.maxHeight = "0px";

  window.menutoggle = function () {
    if (!MenuItems) return;
    if (MenuItems.style.maxHeight === "0px") {
      MenuItems.style.maxHeight = "200px";
    } else {
      MenuItems.style.maxHeight = "0px";
    }
  };

  // ----- Product Gallery -----
  var ProductImg = document.getElementById("ProductImg");
  var SmallImg = document.getElementsByClassName("small-img");

  for (let i = 0; i < SmallImg.length; i++) {
    SmallImg[i].onclick = function () {
      if (ProductImg) ProductImg.src = SmallImg[i].src;
    };
  }

  // ----- Quantity Input -----
  const qty = document.getElementById("qty");
  if (qty) {
    qty.addEventListener("input", () => {
      const value = Number(qty.value);
      if (Number.isNaN(value) || value < 1) qty.value = 1;
    });

    qty.addEventListener("keydown", (e) => {
      if (e.key === "-" || e.key === "e") e.preventDefault();
      if (e.key === "ArrowDown" && Number(qty.value) <= 1) e.preventDefault();
    });

    qty.addEventListener("wheel", (e) => {
      if (qty.value <= 1 && e.deltaY > 0) e.preventDefault();
    });
  }

  // ----- Login/Register Toggle -----
  var LoginForm = document.getElementById("LoginForm");
  var RegForm = document.getElementById("RegForm");
  var Indicator = document.getElementById("Indicator");

  window.register = function () {
    if (LoginForm && RegForm && Indicator) {
      LoginForm.style.left = "-300px";
      RegForm.style.left = "0px";
      Indicator.style.transform = "translateX(100px)";
    }
  };

  window.login = function () {
    if (LoginForm && RegForm && Indicator) {
      LoginForm.style.left = "0px";
      RegForm.style.left = "300px";
      Indicator.style.transform = "translateX(0px)";
    }
  };
  
});
