// Initialize the cart variable
if (localStorage.getItem('cart') == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem('cart'));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
}

// Add an event listener to the "Add to Cart" buttons
$('.cart').click(function() {
  var id = $(this).attr('id');
  var name = $(this).data('name');
  var image = $(this).data('img');
  
  if (cart[id] == undefined) {
    cart[id] = {'name': name, 'image': image, 'quantity': 1};
  } else {
    cart[id]['quantity']++;
  }
  
  localStorage.setItem('cart', JSON.stringify(cart));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
});

// Get the number of items in the cart
function getCartItemCount(cart) {
  var itemCount = 0;
  for (var id in cart) {
    itemCount += cart[id]['quantity'];
  }
  return itemCount;
}

// Display the items in the cart
function displayCartItems(cart) {
  var cartList = document.getElementById('cart-list');
  cartList.innerHTML = '';
  
  for (var id in cart) {
    var item = cart[id];
    var li = document.createElement('li');
    var img = document.createElement('img');
    img.src = item['image'];
    li.appendChild(img);
    li.innerHTML += item['name'] + ' x ' + item['quantity'];
    cartList.appendChild(li);
  }
}

// Display the items in the cart on page load
if (localStorage.getItem('cart') != null) {
  var cart = JSON.parse(localStorage.getItem('cart'));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
  displayCartItems(cart);
}

// Handle the checkout button click
$('#checkout-btn').click(function() {
  // Get the CSRF token from the cookie
  const csrftoken = Cookies.get('csrftoken');

  // Send an HTTP POST request to the server
  $.ajax({
    url: '/checkout',
    type: 'POST',
    data: {
      'cartData': JSON.stringify(cart),
    },
    headers: {
      'X-CSRFToken': csrftoken, // Include the CSRF token in the header
    },
    success: function(response) {
      // Handle the response from the server
      cart = {};
      localStorage.setItem('cart', JSON.stringify(cart));
      document.getElementById('cart').innerHTML = getCartItemCount(cart);
      displayCartItems(cart);
      console.log(response);
      // Update the content of the response message element
      $('#response-message').text("Successfully sent the order");
    },
    error: function(xhr) {
      // Handle any errors
      console.log(xhr.responseText);
    }
  });
});
