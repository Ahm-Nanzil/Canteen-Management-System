const form = document.getElementById('msg-verify');
  const responseMessage = document.getElementById('response-message-contact');

  form.addEventListener('submit', function(e) {
    e.preventDefault(); // prevent the form from submitting normally
    
    const data = new FormData(form); // create a new FormData object with the form data
    console.log(data);
    fetch('/contact', { // replace '/contact' with the URL of your Django view
      method: 'POST',
      body: data
    })
    .then(response => response.json()) // parse the JSON response
    .then(json => {
      // update the response message element with the JSON data
      responseMessage.textContent = JSON.stringify(json);
    })
    .catch(error => {
      // handle any errors
      console.error(error);
    });
  });