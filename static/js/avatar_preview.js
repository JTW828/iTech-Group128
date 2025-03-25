document.addEventListener("DOMContentLoaded", function () {
    const avatarUpload = document.getElementById("avatar-upload");
    const avatarPreview = document.getElementById("avatar-preview");

    if (avatarUpload) {
        avatarUpload.addEventListener("change", function (event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function () {
                    avatarPreview.src = reader.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }
});
