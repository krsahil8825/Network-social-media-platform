document.addEventListener("DOMContentLoaded", function () {
    const followForm = document.querySelector('form[action$="follow_toggle/"]');
    if (followForm) {
        followForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const url = followForm.action;
            const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

            fetch(url, {
                method: "POST",
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.status === "followed") {
                        followForm.querySelector("button").textContent = "Unfollow";
                    } else if (data.status === "unfollowed") {
                        followForm.querySelector("button").textContent = "Follow";
                    }
                })
                .catch((error) => console.error("Error:", error));
        });
    }
});
