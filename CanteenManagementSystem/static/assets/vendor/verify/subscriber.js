const subscriberForm = document.getElementById('subscriber');
    const responseMessageFromSubscribeView = document.getElementById('response-message-subscriber');
  
    subscriberForm.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const formData = new FormData(subscriberForm);
      console.log(formData);
      fetch('/subscribe', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          responseMessageFromSubscribeView.innerText = data.message;
          if (data.success) {
            subscriberForm.reset(); // reset the form if submission is successful
          }
        })
        .catch(error => {
          responseMessageFromSubscribeView.innerText =  data.message;
        });
    });