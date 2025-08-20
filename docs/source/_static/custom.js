function updateFooter() {
    const builtWith = document.querySelector(".wy-footer .rst-footer small");
    if (builtWith) {
        builtWith.textContent = "Your Online Documentation hub is your knowledge source to better know application functionality.";
    } else {
        // Retry every 100ms if the footer is not yet loaded
        setTimeout(updateFooter, 100);
    }
}

// Run the function
updateFooter();
