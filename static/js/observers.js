

/* Code in this file comes from these tutorials for intersection observers
1. https://www.youtube.com/watch?v=T8EYosX4NOo&t=291s
2. https://www.youtube.com/watch?v=RxnV9Xcw914&t=24s
3. https://www.youtube.com/watch?v=huVJW23JHKQ
 It has been slightly modified for my needs to fit my elements that im using it on. 
 But the bulk of the code is from these sources */

const mainNav = document.querySelector(".main-navbar");
const mainNavBurger = document.querySelector(".mainNav-burger")
const smallBurgerMenu = document.querySelector(".burgerMenu-bg-clr")

const pageIntro = document.querySelector(".page-main-intro");

const faders = document.querySelectorAll('.fade-in');
const sliders = document.querySelectorAll('.slide-in');

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

const appearOptions = {
    threshold: 0,
    rootMargin: "0px 0px -100px 0px"
};

// Create new intersection observer for the products
const appearOnScroll = new IntersectionObserver
(function(
        entries, 
        appearOnScroll
    ) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('appear');
                appearOnScroll.unobserve(entry.target);
            }

        });
    }, 
    appearOptions);


faders.forEach(fader => {
    appearOnScroll.observe(fader);
});

sliders.forEach(slider => {
    appearOnScroll.observe(slider)
});

