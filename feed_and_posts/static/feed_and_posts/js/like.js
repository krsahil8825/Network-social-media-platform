document.addEventListener("DOMContentLoaded", function () {
    const likeForms = document.querySelectorAll(".like-form");

    likeForms.forEach((form) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const slug = form.querySelector('input[name="slug"]').value;

            fetch(form.action, {
                method: "POST",
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.liked !== undefined) {
                        const likeIcon = form.querySelector("i");
                        likeIcon.className = data.liked ? "bi bi-heart-fill text-danger" : "bi bi-heart";
                    }
                })
                .catch((error) => console.error("Error:", error));
        });
    });
});
