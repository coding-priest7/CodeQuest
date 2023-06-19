const show5Btn = document.getElementById("show5");
const show10Btn = document.getElementById("show10");
const show20Btn = document.getElementById("show20");
const themeToggle = document.getElementById("themeToggle");
const linksContainer = document.getElementById("links-container");

show5Btn.addEventListener("click", () => {
  displayLinks(5);
});

show10Btn.addEventListener("click", () => {
  displayLinks(10);
});

show20Btn.addEventListener("click", () => {
  displayLinks(20);
});

themeToggle.addEventListener("change", () => {
  if (themeToggle.checked) {
    document.body.classList.add("dark-theme");
  } else {
    document.body.classList.remove("dark-theme");
  }
});

// Get the image boxes
const imageBoxes = document.querySelectorAll(".image-box");

// Function to show the specified number of results
function showResults(numResults) {
  // Hide all image boxes
  imageBoxes.forEach((box) => {
    box.style.display = "none";
  });

  // Show the desired number of image boxes
  for (let i = 0; i < numResults; i++) {
    if (imageBoxes[i]) {
      imageBoxes[i].style.display = "block";
    }
  }
}

function displayLinks(num) {
  linksContainer.innerHTML = ""; // Clear previous links

  for (let i = 0; i < num && i < results.length; i++) {
    const result = results[i];
    const link = document.createElement("a");
    link.href = result["Question Link"];
    link.textContent = result["Question Link"];
    linksContainer.appendChild(link);
  }
}
