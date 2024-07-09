document.addEventListener("DOMContentLoaded", () => {
  const mainImg1 = document.getElementById("main-img-1");
  const mainImg2 = document.getElementById("main-img-2");
  const thumbnails = document.querySelectorAll(".thumbnail");
  const mainColorDiv = document.getElementById("main-color");
  const selectedColorName = document.getElementById("selected-color-name");

  thumbnails.forEach((thumb) => {
      thumb.addEventListener("click", () => {
          const newSrc1 = thumb.getAttribute("data-src-1");
          const newSrc2 = thumb.getAttribute("data-src-2");
          const newColor = thumb.querySelector('.color').style.backgroundColor;
          const colorName = thumb.getAttribute("data-name");

          mainImg1.src = newSrc1;
          mainImg2.src = newSrc2;
          mainColorDiv.style.backgroundColor = newColor;
          selectedColorName.textContent = colorName;
      });
  });
});