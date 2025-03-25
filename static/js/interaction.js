document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function () {
            const storeId = this.getAttribute("data-store-id");
            const icon = this.querySelector(".like-icon");

            fetch(`/store/${storeId}/like/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                this.querySelector(".like-count").textContent = data.like_count;

                if (data.liked) {
                    icon.classList.remove("fa-regular", "not-liked");
                    icon.classList.add("fa-solid", "liked");
                    icon.style.color = "red";  // 变红
                } else {
                    icon.classList.remove("fa-solid", "liked");
                    icon.classList.add("fa-regular", "not-liked");
                    icon.style.color = "black";  // 变回黑色空心
                }
            });
        });
    });

    document.querySelectorAll(".favourite-btn").forEach(button => {
        button.addEventListener("click", function () {
            const storeId = this.getAttribute("data-store-id");
            const icon = this.querySelector(".favourite-icon");

            fetch(`/store/${storeId}/favourite/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                this.querySelector(".favourite-count").textContent = data.favourite_count;

                if (data.favourited) {
                    icon.classList.remove("fa-regular", "not-favourited");
                    icon.classList.add("fa-solid", "favourited");
                    icon.style.color = "gold";  // 变金色
                } else {
                    icon.classList.remove("fa-solid", "favourited");
                    icon.classList.add("fa-regular", "not-favourited");
                    icon.style.color = "black";  // 变回黑色空心
                }
            });
        });
    });

    function getCSRFToken() {
        return document.cookie.split('; ')
            .find(row => row.startsWith('csrftoken'))
            ?.split('=')[1];
    }
});
