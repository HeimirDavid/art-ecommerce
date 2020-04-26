// tutorial used for intersection observers https://www.youtube.com/watch?v=RxnV9Xcw914


const mainNav = document.querySelector(".main-navbar");

const mainNavBurger = document.querySelector(".mainNav-burger")
const smallBurgerMenu = document.querySelector(".burgerMenu-bg-clr")

const pageIntro = document.querySelector(".page-main-intro");

// negative rootmargin to make sure the observer adds/removes a class to the main nav 100px
// before it's fully in the viewport
mainNavOptions = {
    rootMargin: "-100px 0px 0px 0px"
};

// new intersectionObserver whichs adds/removes a class to change colors of the main navbar when
// it reaches the page content
const mainNavObserver = new IntersectionObserver(function(
    entries,
    mainNavObserver
    ) {
        entries.forEach(entry => {
            if(!entry.isIntersecting) {
                mainNav.classList.add('main-nav-scrolled');
                mainNavBurger.classList.add('burgerScrolled');
                smallBurgerMenu.classList.add('burgerMenu-bg-clr-on-scroll');
            } else {
                mainNav.classList.remove("main-nav-scrolled")
                mainNavBurger.classList.remove('burgerScrolled');
                smallBurgerMenu.classList.remove('burgerMenu-bg-clr-on-scroll');
            }
        })
    },
    mainNavOptions);

mainNavObserver.observe(pageIntro)


/*
var button = document.getElementById("addPrints");
var sizeOne = document.getElementById("sizeOne")
var quantity = document.getElementById("quantity")
var prices = sizeOne.value * quantity.value;
$( document ).ready(function() {
    console.log( "ready!" );



    var sizeOne = $('#sizeOne')
    console.log(sizeOne.value)
});*/

//var sizeOne = document.getElementById("sizeTwo").value;
//console.log(sizeOne)


function getPriceForPrints() {
    var sizeOne = document.getElementById("sizeOne");
    var sizeTwo = document.getElementById("sizeTwo");
    var sizeThree = document.getElementById("sizeThree");
    var sizes = [sizeOne, sizeTwo, sizeThree]

    for(i=0; i < sizes.length; i++) {
        if(sizes[i] === null) {
            sizes.splice(i, 1);
        }
        console.log(sizes[i].value)
    }

}

getPriceForPrints();