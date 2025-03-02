let scrollContainer = document.querySelector(".gallery"); 
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
    scrollContainer.style.scrollBehavior = "auto"; // Instant scrolling for wheel
});

nextBtn.addEventListener("click", () => {
    scrollContainer.style.scrollBehavior = "smooth"; // Smooth for button clicks
    scrollContainer.scrollLeft += 900;
});

backBtn.addEventListener("click", () => {
    scrollContainer.style.scrollBehavior = "smooth"; // Smooth for button clicks
    scrollContainer.scrollLeft -= 900;
});
