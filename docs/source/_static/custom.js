document.addEventListener("DOMContentLoaded", function() {
    // create a new link element
    var logoLink = document.createElement("a");
    logoLink.href = "/"; // change this to your homepage if needed
    logoLink.style.position = "absolute";
    logoLink.style.top = "10px";   // adjust
    logoLink.style.right = "10px"; // adjust
    logoLink.style.width = "32px";
    logoLink.style.height = "32px";
    logoLink.style.display = "block";

    // create an img element inside the link
    var img = document.createElement("img");
    img.src = "_static/my_logo.png";
    img.style.width = "100%";
    img.style.height = "100%";
    img.style.objectFit = "contain";

    logoLink.appendChild(img);

    // append to the top header
    var header = document.querySelector(".wy-nav-top");
    if(header) {
        header.appendChild(logoLink);
    }
});

