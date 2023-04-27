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
    if (cart[idstr] != undefined) {
      cart[idstr] = cart[idstr] + 1;
    } else {
      cart[idstr] = 1;
    }
    console.log('cart:', cart);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = getCartItemCount(cart);
  });
  
  function getCartItemCount(cart) {
    var cartItems = Object.values(cart);
    var itemCount = cartItems.reduce(function(total, current) {
      return total + current;
    }, 0);
    return itemCount;
  }
  