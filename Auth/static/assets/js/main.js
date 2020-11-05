let products = [];
let temp=[];
p=document.querySelectorAll(".product");
console.log(p);
for(i=0;i<p.length;i++){
    let title=p[i].querySelector(".card-title").innerHTML;
    let detail=p[i].querySelector(".card-text").innerHTML;
    let slug=p[i].querySelector(".card-slug").innerHTML;
    let id=p[i].querySelector(".card-id").getAttribute("data-product-id");
    temp.push({'title':title,'detail':detail,'slug':slug,'id':id,'quantity':0});
}
products=temp;
console.log(temp);

function renderCart(cart) {
    const cartList = document.getElementById('cart-list');
  
    if (cart.length === 0) {
      cartList.innerHTML = 'هیچ ایتمی در سبد خرید شما وجود ندارد.';
      return;
    }
  
    const cartHTML = cart
      .map(
        item =>
          `<div
                  class="list-group-item d-flex justify-content-between align-items-center cart-item"
              >
                  <span>${item.title}</span>
                  <div>
                      <button class="btn inc-quantity" data-product-id="${item.id}">+</button><span>${item.quantity}</span
                      ><button class="btn dec-quantity" data-product-id="${item.id}">-</button>
                  </div>
              </div>`
      )
      .join('');
  
    cartList.innerHTML = cartHTML;
  }
  
  function addToCart(productId, products, cart) {
    const addedProduct = products.filter(product => product.id == productId)[0];
    console.log(products);
    console.log(addedProduct);
    const productInCart = cart.find(item => item.id == productId);
  
    if (productInCart) {
      return cart.map(item =>
        item.id == productId ? {...item, quantity: item.quantity + 1} : item
      );
    }
  
    return [...cart, {...addedProduct, quantity: 1}];
  }
  
  function takeFromCart(productId, cart) {
    const productInCart = cart.find(item => item.id == productId);
  
    if (productInCart.quantity === 1) {
      return cart.filter(item => item.id != productId);
    } else {
      return cart.map(item =>
        item.id == productId ? {...item, quantity: item.quantity - 1} : item
      );
    }
  }
  
  function presistCart(cart) {
    window.localStorage.setItem('cart', JSON.stringify(cart));
  }
  
  function rehydrateCart() {
    if (window.localStorage.getItem('cart')) {
      return JSON.parse(window.localStorage.getItem('cart'));
    } else {
      return [];
    }
  }
  
  let cart = [];
  
  cart = rehydrateCart();
  
  renderCart(cart);
  
  document.addEventListener('click', function (e) {
    if (e.target && e.target.classList.contains('add-to-cart')) {
        console.log('click');
      const productId = e.target.getAttribute('data-product-id');
      console.log(productId);
      cart = addToCart(productId, products, cart);
      console.log(cart);
      renderCart(cart);
      presistCart(cart);
    } else if (e.target && e.target.classList.contains('inc-quantity')) {
      const productId = e.target.getAttribute('data-product-id');
      console.log(productId);
      cart = addToCart(productId, products, cart);
      renderCart(cart);
      presistCart(cart);
    } else if (e.target && e.target.classList.contains('dec-quantity')) {
      const productId = e.target.getAttribute('data-product-id');
      cart = takeFromCart(productId, cart);
      renderCart(cart);
      presistCart(cart);
    }
  });