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


//Get the price for the print and quantity of a specific print the user has picked

function getPriceForPrints() {
    var selectOptions = document.getElementById("sizeOptions").value;
    var quantity = document.getElementById("quantity").value;
    var priceForPrints = parseFloat(selectOptions * quantity).toFixed(2);
    
    if(isNaN(priceForPrints) || priceForPrints == 0) {
        document.getElementById('displayPrice').innerHTML = "You need to pick both a size and wished number of prints.";
        document.getElementById('currency-euro').innerHTML = "";
    } else {
        document.getElementById('displayPrice').innerHTML = priceForPrints;
        document.getElementById('currency-euro').innerHTML = "€";
    };
};

