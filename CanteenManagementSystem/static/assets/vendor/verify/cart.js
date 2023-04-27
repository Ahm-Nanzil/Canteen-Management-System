if (localStorage.getItem('cart') == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem('cart'));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
}

$('.cart').click(function(){
  console.log('clicked');
  var idstr = this.id.toString();
  console.log('idstr:', idstr);
  var name = $(this).data('name');
  var img = $(this).data('img');
  console.log('name:', name);
  console.log('img:', img);
  if (cart[idstr] != undefined) {
      cart[idstr].quantity = cart[idstr].quantity + 1;
  } else {
      cart[idstr] = {
          name: name,
          image: img,
          quantity: 1
      };
  }
  console.log('cart:', cart);
  localStorage.setItem('cart', JSON.stringify(cart));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
});

function getCartItemCount(cart) {
  var itemCount = 0;
  for (var id in cart) {
      itemCount += cart[id].quantity;
  }
  return itemCount;
}
// display cart item

function displayCartItems(cart) {
  var cartList = document.getElementById('cart-list');
  cartList.innerHTML = '';

  for (var id in cart) {
    var item = cart[id];
    var li = document.createElement('li');
    var img = document.createElement('img');
    img.src = item.image;
    li.appendChild(img);
    li.innerHTML += item.name + ' x ' + item.quantity;
    cartList.appendChild(li);
  }
}

if (localStorage.getItem('cart') == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem('cart'));
  document.getElementById('cart').innerHTML = getCartItemCount(cart);
  displayCartItems(cart);
}

$('.cart').click(function(){
  // ...
  displayCartItems(cart);
  // ...
});

// Checkout order

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
    },
    error: function(xhr) {
      // Handle any errors
      console.log(xhr.responseText);
    }
  });
});
