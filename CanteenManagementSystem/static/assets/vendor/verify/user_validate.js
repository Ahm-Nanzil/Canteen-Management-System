const formSignUp = document.getElementById('signup-form');
    const responseMessageFromUser = document.getElementById('response-message');
  
    formSignUp.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const formData = new FormData(formSignUp);
      console.log(formData);
      fetch('/signup', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          responseMessageFromUser.innerText = data.message;
          if (data.success) {
            formSignUp.reset(); // reset the form if submission is successful
          }
        })
        .catch(error => {
          responseMessageFromUser.innerText = 'An error occurred. Please try again.';
        });
    });