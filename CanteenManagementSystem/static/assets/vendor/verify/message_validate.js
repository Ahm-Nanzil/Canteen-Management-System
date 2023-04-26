const form = document.getElementById('msg-verify');
const responseMessage = document.getElementById('response-message-contact');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);

  fetch('/contact', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      responseMessage.innerText = data.message;
    })
    .catch(error => {
      responseMessage.innerText = 'An error occurred. Please try again.';
    });
});
