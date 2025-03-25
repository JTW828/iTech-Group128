document.addEventListener("DOMContentLoaded", function() {
    let index = 0;
    const images = document.querySelectorAll(".carousel-item");

    function changeSlide() {
        images.forEach((img, i) => {
            img.style.opacity = (i === index) ? "1" : "0";
        });
        index = (index + 1) % images.length;
    }

    setInterval(changeSlide, 3000); // 3秒切换
});
