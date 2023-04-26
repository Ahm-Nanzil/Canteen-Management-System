const form = document.getElementById('signup-form');
    const responseMessage = document.getElementById('response-message');
  
    form.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const formData = new FormData(form);
  
      fetch('/signup', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          responseMessage.innerText = data.message;
          if (data.success) {
            form.reset(); // reset the form if submission is successful
          }
        })
        .catch(error => {
          responseMessage.innerText = 'An error occurred. Please try again.';
        });
    });