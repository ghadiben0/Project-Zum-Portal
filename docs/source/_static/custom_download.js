function addDownloadButton(flyout) {
  if (!flyout.querySelector('.download-button')) {
    const downloadButton = document.createElement('button');
    downloadButton.className = 'download-button';
    downloadButton.innerText = 'Download';
    Object.assign(downloadButton.style, {
      height: '40px',
      width: '100%',
      backgroundColor: '#f1f3f4',
      borderRadius: '8px',
      border: '1px solid #ccc',
      fontSize: '14px',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      marginBottom: '12px',
    });

    downloadButton.addEventListener('click', () => {
      window.location.href = '/path/to/file.pdf';
    });

    // Add the button at the top of the Flyout
    flyout.prepend(downloadButton);
  }
}

// Observe the body for added nodes (like the Flyout)
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    mutation.addedNodes.forEach((node) => {
      if (node.nodeType === 1 && node.matches('.flyout')) { // adjust selector if needed
        addDownloadButton(node);
      }
    });
  });
});

observer.observe(document.body, { childList: true, subtree: true });

// Optional: in case Flyout already exists at page load
document.querySelectorAll('.flyout').forEach(addDownloadButton);
