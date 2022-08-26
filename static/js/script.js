



/**
 * navbar toggle
 */

const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const overlay = document.querySelector("[data-overlay]");

const elemArr = [navCloseBtn, overlay, navOpenBtn];

var clk = document.getElementById('contat');
var like1 = document.getElementById('like');


var letras = document.getElementById('amei'); // ou:
var vk = document.getElementById('vk');




/*
 * Click contato final PAGE.

*/

clk.addEventListener('click', function() 
{
  $(document).scrollTop($(document).height());
});



/*
 * Click like PAGE.

*/




like1.addEventListener('click', function() 
{
  letras.style.color = '#0cb2ea';
  letras.textContent = "402 VOCÊ CURTIU!!"
});






/*
 * Click vakinha PAGE.

*/




vk.addEventListener('click', function() 
{
  window.location.href = "https://nubank.com.br/pagar/rbb9r/trxGp4Gfrx";

});



for (let i = 0; i < elemArr.length; i++) {
  elemArr[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
  });
}

/**
 * toggle navbar & overlay when click any navbar-link
 */

const navbarLinks = document.querySelectorAll("[data-navbar-link]");

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
  });
}





/**
 * header & go-top-btn active
 * when window scroll down to 400px
 */

const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {
  if (window.scrollY >= 400) {
    header.classList.add("active");
    goTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    goTopBtn.classList.remove("active");
  }
});


