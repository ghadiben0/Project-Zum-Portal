document.addEventListener("DOMContentLoaded", function() {
    // Select the flyout menu container
    const flyoutMenu = document.querySelector(".wy-side-nav-search"); // adjust if needed

    if (flyoutMenu) {
        // Create the Download dropdown
        const downloadDiv = document.createElement("div");
        downloadDiv.className = "wy-dropdown custom-downloads";

        // Add the button and dropdown links
        downloadDiv.innerHTML = `
            <button class="wy-btn wy-btn-small">Download</button>
            <ul class="wy-dropdown-content">
                <li><a href="_build/pdf/YourProject.pdf" target="_blank">PDF</a></li>
                <li><a href="_build/html/index.html" target="_blank">HTML</a></li>
                <li><a href="_build/epub/YourProject.epub" target="_blank">EPUB</a></li>
            </ul>
        `;

        // Append the Download button to the flyout
        flyoutMenu.appendChild(downloadDiv);
    }
});
