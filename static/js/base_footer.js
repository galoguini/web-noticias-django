document.addEventListener("DOMContentLoaded", function () {
    var mainContentWrapper = document.getElementById("main-content-wrapper");
    var footer = document.querySelector("footer");

    window.addEventListener("scroll", function () {
        var scrollPosition = window.scrollY + window.innerHeight;
        var pageHeight = document.body.offsetHeight;

        if (scrollPosition >= pageHeight) {
            footer.style.display = "block";
        } else {
            footer.style.display = "none";
        }
    });
});