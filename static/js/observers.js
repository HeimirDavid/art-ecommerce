// tutorial used for intersection observers https://www.youtube.com/watch?v=RxnV9Xcw914


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


const appearOnScroll = new IntersectionObserver
(function(
        entries, 
        appearOnScroll
    ) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                console.log("damn")
                return;
            } else {
                console.log("jibbicola")
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

