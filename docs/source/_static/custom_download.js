document.addEventListener('DOMContentLoaded', () => {
  const flyout = document.querySelector('.flyout'); // adjust selector if needed
  if (!flyout) return;

  const downloadButton = document.createElement('button');
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

  flyout.prepend(downloadButton);
});
