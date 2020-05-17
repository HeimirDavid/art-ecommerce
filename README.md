
# Sandra Löwgren Art Gallery and E-Commerce

SL Gallery is a Gallery and E-commerce where you can browse and buy original paintings or prints
from the artist Sandra Löwgren. There is also a blog/news section where you can keep up to date with the
latest from the artist!

## UX

**User Stories**

* As an artist, I want a good looking website where I can display my paintings efficiently, so I can grow
my buissness and sell both original work and prints of my paintings.
* As an artist, I want a place to display news about upcoming exhibitions, or new art that im working on.
* As an artist, I wish to be able to sell prints if the original painting is already sold.
* As a fan, I want to find paintings from the artist and browse through the gallery.
* As a customer, I wish to be able to buy art from the artist.
* As a customer, I wish to have the ability to buy prints of paintings in different sizes.
* As a fan/customer, I wish to learn more about the artist and the paintings she provides.

### Strategy

The main goal for this website is to display the art from the artist in an elegant way with good looking design 
to raise her brand and provide value by selling both original paintings and prints.

### Scope

For users who are looking to get to know both the artist and her art better they can do that by reading about the 
paintings, the different collections they belong to, and different upcoming events and news from the artist. This 
provides value for both the fans of the artist and users who are new to the artist. If a user see some painting they like, it should be easy to order it straight away.

### Structure

* ***The landing page*** displays an about section and a little of everything. So if a user visits the site, they find both about, news, and paintings there. 

* ***The paintings section*** is where all the paintings are. They are displayed with an image, name and a description, as well as if they are availible as original work, print or both. Here you can filter the paintings by which collection they belong to, also with information about the chosen collection.

* ***The news section*** is where all the articles goes. Pretty straight forward blog post style, with the most recent being displayed first.

* ***The contact page*** has a form where a user can input their name, email and a message which will be sent to the artist.

* ***The login/Register*** section is two different pages with two different forms. One to log a user in, and one where a user can create an account which is needed to purchase a painting. Both pages also has a link to the other, if a user might have landed on the wrong one.

***The cart*** is only accessable if a user has put an item in the cart. It displays a table with it's content along with a button to redirect the user to the checkout.

***Checkout*** can be reached at the bottom of the cart. There you fill out three different forms. Billing address, shipping address, and credit card info along with a last look at the order summary. Here different error messages are also displayed if a user puts in invalid info such as invalid date for their credit card, invalid card number, etc.

***The user orders*** can be reached once a user is logged in and has purchased an item. There you can see your purchased painting, order info and the status of their order.

***The orders section*** can only be accessed by the superuser/admin. Here the artist can see the orders made by the customers. It displayes the most crucial info in a table, along with a link to each individual order where all the info about that order exists.

***FAQ section*** contains some general info a user might ask themself. At the moment it contains shipping and payment info, along with a link to the contact page if a user has a more specific question. **Note** that this at the moment is purely made up with the shipping costs and shipping time.

### Skeleton
These wireframes were from my first sketch of the website and are not completely as the site turned out. But I tried to stay as close to them as possible and there are just some minor differences. Especially the single product page got some resturcture when it was built.

#### Wireframes
* [base.html](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/base.html.png) - The Header, navigation and footer for all the pages.
* [index page](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/index.png) - The landing page of the website.
* [Paintings](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Store.png) - All the paintings for sale.
* [Paintings with Collection](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Store%20-%20collection.png) - All the paintings that belong to a certain collection when that is filtered.
* [One single product](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Product.png)
* [Contact Page](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Contact.png)
* [Cart page](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Cart.png)
* [Checkout Page](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Checkout.png)
* [Single Article/Blog Post](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/wireframes/Blog%20Post.png)

### Surface

Since this is a foremost a website displaying images of paintings, I choose a quite neutral colour palette with different shades of grey-scale colours, along with some dark blue for the top and the footer. This to not distract the user from the images of the paintings and to keep a clean look of the site.

## Features

 ### Featires implemented

 #### APPS ####

**Handles different apps for different features and parts of the site:**
* The **accounts** app handles the authentication and data of the users.
* The **carts** app handles the logic behind creating a cart, adding items to it and rendering the correct views, as well as models (tables) for the cart and cart items. Each cart can have multiple items, and each product can have different variations of price and size. This depend on whether the product is an original painting or a print. This is the reason to why there is cart item in the cart and not simply the product, the same painting can exist as multiple products. In the views.py the add_to_cart function handles all of this. It checks whether the product is an original painting or print, creates a cart item of this data and adds it to the cart. It also handles errors that can come from the user. Such as choosing a print without a specific size or reversed, choosing a quiantity that is greater than the stock, and making sure that the same product is not added to the cart more than once. This to make sure the order does not exceed the stock of prints, or an original painting, which only excist as one, can be bought multiple times.
* The **checkout** app takes care of the checkout process. This includes providing forms the user needs, validating them and store the data in the userAddress and Order models in the app. Provide the correct error messages if something goes wrong, and rendering the correct templates.
* The **products** app takes care of all the paintings. In the models the product (painting) is stored with it's general info and three more tables which is more specific for the painting. This include the collection it belongs to, the original painting table with the size and price, along with a table for the prints with size and price. In the views.py file the functionality of rendering all the products on one page is handled and categorising them by collection. As well as rendering a single product that is picked by the user.
* The home app takes care of rendering the index page and the two pages that I didn't want to create individual apps for. Those two are the contact page and the FAQ page since they are quite simple.
* The **newsposts** app is the most individual app of the site. The models is simple with one table. The views.py renderes all the articles, ordered by date and individual posts, picked by the user.
* The **orders** app renders the data from the Orders table from the checkout app, and displays it on a few different templates. It makes sure that only a superuser can access all the orders, and that a logged in user can access their own orders and see their status. This is all handled in the views.py file.

 ### Features Left to Implement

 * **Pagination** - at the moment the paintings are quite few and takes a long time to build up stock for. It would've been a good idea to implement it now but due to it not having the highest priority and the deadline coming closer, I choose to leave it for future implementation.
 * **Site owner input** - At the moment all the input of products, collections, prints and articles are input through the django admin panel. This works fine, but it would be more elegant for the owner of the site to have their own interface to interact with to input all of this data. Including changing the status of an order as well.
 * **Registered User Functionality** - allow a user to log in via their email and change their password.
 * **Address** - Since both the billing and shipping address is stored it would be great for an existing customer to be able to choose their previously used address from a dropdown when they go to the checkout.
 * **Cart Timeout** - It would be good to integrate a timeout on the original paintings. So if an original painting is added to a cart, it would be set aside for that customer for maybe 5-10 minutes.


## Technologies Used
* HTML, CSS, JS, Python where the core languages used to create this website.
* [Django 3.0.5](https://www.djangoproject.com/) - web framework.
* [Stripe](https://stripe.com/) - online payments platform. Their API used to validate and handle secure payments with credit card.
* [EmailJS](https://www.emailjs.com/) - Their JavaScript API used to send emails to the artist through the contact form.
* [Amazon Web Services](https://aws.amazon.com/) - AWS S3 Bucket for storing the media and static files.
* [Heroku](https://www.heroku.com/) - Hosting the live project.
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Image library to handle the media upload.
* [Django forms bootstrap](https://pypi.org/project/django-forms-bootstrap/) - To format the django forms as bootstrap.
* [Fancybox](http://fancyapps.com/fancybox/3/) - Used to display the images as full view.
* [Bootstrap 4](https://getbootstrap.com/) - Used for their responsive css grid and basic styling for forms, buttons and tables.
* [jQuery](https://jquery.com/) - For simplifying DOM manipulation.
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - template language for Python.
* [Lucidchart](https://www.lucidchart.com/) - To draw the Entity Relationship Diagram.


### Databases
SQLite was used during development as it is Django's default database. PostgreSQL used for the deployed version and installed as an add-on in the Heroku dashboard for the application.
* [Entity-relationship diagram](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/erd/art-store-erd.png) - Here is the diagram over my database design. The cart and cart-item tables came a bit later as I had to go back to the drawing board when I switched to saving it in the database instead of using sessions. This was mainly due to the layout of the products and their variations. Every product has an original painting, but the prints and the original does not have the same prices. So every time a user adds a product to the cart, the product needs to be checked if it is a print or original and get the foreign key for it. Due to the fact that I had more experience with working with models in django I decided to design it this way instead of saving it all in sessions.


## Testing
The features and functionality of this site has been tested almost only manually. A few unit test were written to test the urls and the simplest views but that was mainly for me personally to try it out as I lack experience in it. Otherwise the main principle throughout this projct has been regression testing after each added feature or functionality.  
A regular test after each modifiation would include:
* Does the page still load?
* Does the layout still looks the same or as intended and is it responsive for different sizes?
* Does the menu buttons still work?
* Does the links and button in the site still work?
* Can I still input data in the admin panel?
* Does that data output on the site?
* Can I register a new user, login and logout?
* Does the correct data that is accessable for the user match with the users current authentication status?
* Can I add an item to the cart?
* Can I procceed to checkout?
* Can I purchase an item and view it in my orders?
* Can the admin see all the orders?

#### Cart

The carts app's models have been tested with inputing data into the django admin panel, and modifing it and deleting data to see that the relationship between the cart table and cart-items table work as intended.  
Adding an item to the cart is not as forward as simply pressing a button since it is multiple choices that is expected from a user.   
Testing the cart and making sure that the correct item that the user wishes to add is done correcly would include:
* If a user adds an original painting to the cart, is it the correct item and painting that gets added?
* If a user tries to add the original work once more, does it get redirected to the correct place with correct error message?
* If a user adds a print to the cart, does the correct print with size and correct quantity adds to the cart?
* If a user press the 'add print to cart' button, but has not picked a size or quantity, does the site redirect with correct error message to the user?
* If one of the two is missing, size or quantity, does it also redirect with correct message?
* If a user tries to add a quantity that exceeds the existing stock of a print, does it also give the correct error message with a redirect back to the product?
* If a user tries to add the exact same print twice to the cart does it also redirect back with correct message? (mentioned more below)
* if a user has a print with the size medium, can it still add all other variations of the item to the cart?

**Cart - Stock**
  
All prints and original paintings have a stock row in their tables. If a user adds 50 prints of a painting to the cart, and the stock is 60 there is no problem. But if a user adds the same print twice, maybe by an accident and this time 20, the total in the cart would exceed the stock. To deal with this issue I added a functionality to the add_to_cart function in the views.py file to check if the item that is being added aleady exist in the cart and redirect the user back to the product with a message to notifify the user that the item is already in their cart. In the future it might be more elegant to allow the user to simply adjust the quantity of the item instead of blocking it completely.   

**Cart bugs** - Two main bugs came up when I modified the existing function to work with this stock integration and control that every print has a quantity and size. 
* First was that everytime a user got redirected with an error message, the requested item did not add to the cart (which is correct), but an original painting did add to the cart without adding to the total of the cart. After lots of testing I discovered that this was due to the fact that the cart was created at the top of the function so every time a test failed later on, it was already created with an assosiated product. ```cart_item = CartItem.objects.create(cart=cart, product=product)``` This code was then moved down to the end when all the controls had already been made.
* Second was that if an original painting was added to the cart, no print of the same painting could be added. This I realised was because when I checked if the item was already in the cart, I was comparing the id of the requested items' print_id with the current products in the cart. This did not work since all prints are associated with a product, and each product has an original painting. So I needed to loop through the items in the cart, see if they have a print_variation, if not the product is an original painting and does can not match with the print. If it has a print_variation id, check that id with the current item and it's print_id and if it matches the items are the same.  

**Bugs - sidenote**   
This above is a good example of alot of issues I encoutered when handling the products. Since the product is not the most relevant, but the original painting/prints were and they both have different relationship with the products table (one-to-many or one-to-one). So everytime a product is handled in the cart, checkout, orders or simply in the html, there is always controls to check if the product is a print or original. Now, with a bit more experience, this could maybe have been estimated as an issue early on and perhaps the database design could have looked a bit differently. But as for now it all works fine, and I learned alot about querying from different tables with different relationships using django.
   
**Stock - sidenote**  
Since this is still just for educational purpose and will not (yet) be used as a real ecommerce, the stock integration stop at the cart. Meaning buying a product does not reduce the stock right now.

#### Forms
All forms have been tested at the checkout, login and register. A required field cannot be left out, error message appears when a field is missing for an address as an example. The correct data from the user is saved to the database, address and it's type (shipping or billing), or registered user.  

**Register/login**   
* Two users can not have the same username.
* Two users can not have the same email address.
* When a user creates an account, the passwords must match.
* All django password error handling gets displayed, their requirements for a password. For example if a password is too common, to long/short.

#### Stripe - checkout
Stripe error messages displays when an error with the payment occurs. Examples are: could not find payment information, invalid card number, expired date etc. This gets displayed using a bootstrap alert style in the payment form.
If a payment goes through, the user gets redirected to the home page with a success message, and their order is vissible to them in the 'my orders' section in the main navigation. The order is saved and the payment is vissible in the stripe dashboard.  
  
**Note:** This website is for educational purpose and to test the payments in this application, use the Stripe test card numbers [here](https://stripe.com/docs/testing#cards).
As I tested this myself the test card that has been used was:  
* card number: 4242424242424242
* CVV: Any 3 digits
* Exipry Dates: Any future date availible
  
#### Contact
The contact form uses emailJS to send an email. If any required field is left out, it does not submit. If the email address is not valid, it does not submit. If for some reason the email does not send through, this is displayed with an alert to the user. If the email does send, the user gets an bootstrap alert informing the user that the message is sent.

#### Responsiveness
This site has been tested on multiple devices and browsers. **Browsers including:** Microsoft Edge, Safari, Chrome, Samsung Internet. **Devices including:** Android phone and IOS, ipad, windows computer with resolution 1920 x 1080 on which the site was developed. The responsiveness of the site was tested throughout the develoment using chrome developer tools. The main testing on other devices was made after the first deployment. This resolved one main issue. On mobile devices there were maybe a 10% white space to the right of the viewport. After some research I found out that ```overflow-x: hidden``` does not work on the body on mobile devices. To work around this I put a div with the styling of overflow hidden instead around the content block in the base.html file. This removed all overflow on smaller devices as intended.

### Code Validation
* All **html** files have went through the W3C validator. The main warning I got from it were on all the jinja syntax. Just got a few warnings with forms that had empty action tags which were removed. Otherwise not much editing were done to the html after going through the validation.
* The **CSS** went through the W3C jigsaw validator as well and came out without any errors or warnings.
**PEP8** - Not all .py files went through the validation, but the largest and most important did. Mainly the views.py for the carts, accounts and checkout apps. The main warnings were whitespace, too long lines and comments without a whitespace between the comment and the # symbol. Almost all of these warnings I did something about. Removing withspace, moving one line to multiple lines, adding whitespace in comments etc. A few warnings I ignored when the line was maybe just a character over the recomended length.
**jshint** - The sendEmailJS.js and observers.js files went through the jshint validator. A few missing semicolons, and one variable missing a declaration were the warnings. These have been modified to pass the test.

## Deployment

#### The steps I took to deploy this project where:
* Pushing the code from my terminal window to Github.
* Created a new S3 Bucket on AWS web services to host the static and media files.
* Creating a new app on the Heroku platform and deploying it from the github repository.
* Set the secret environment variables to the Config Vars in the settings page of the heroku app for live deployment. The same ones that are in the env.py file.
* In the 'Deploy' tab in the dashboard, deploy from the master branch.

#### Run the project locally

You must have the following installed to run this locally:
* Latest version of Python
* Git
* Working IDE, I used Visual Studio Code for there steps.
* Visual studio extension for python. Named Python From Microsoft.

#### Clone the repository

1. Go to https://github.com/HeimirDavid/art-ecommerce
2. Press the button "Clone or Download" to the right.
3. Press "Use HTTPS" and copy the URL from the text field.
4. Create a folder for your workspace in Visual Studio Code.
5. Open a terminal window and navigate to the directory you wish to put this project.
6. type git clone followed by the copied URL.

#### Set up the workspace
1. Open a terminal window from your computer.
2. Locate the workspace directory.
3. Create a viritual environment by typing ```py -m venv env``` into the command prompt. Folder "env" should now be installed in the workspace.
4. Activate the environment by typing env\Scripts\activate.
5. Install the required packages from requirements.txt by typing ```pip install -r requirements.txt```.
6. Make sure to set up the environment variables in an env.py file and add it to .gitignore.
7. Type ```python manage.py runserver``` to run your local server and go to the URL provided in your terminal window.

## Credits
* [Django Ecommerce Web application](https://www.youtube.com/watch?v=fhATkPoU22k&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK) - I found this tutorial playlist on youtube from the channel Coding Point. I used it to get inspiration and find soloutions for some of my problems with the cart, product variations and checkout. I built the base functionality for the carts app and part of the checkout app based on this series. Especially the views.py file in the carts app. Since it's over 80 clips I haven't looked through them all, just the ones that were a part about the cart and checkout. Episodes 22-33, 35-38 and 69-72.
* [Intersection Observers](https://www.youtube.com/watch?v=T8EYosX4NOo&t=291s) - After looking around for different simple soloutions to create some animations without using event listeners I found this tutorial on intersection observers. Part one of a three series tutorial.
* [Intersection Observers - Navbar](https://www.youtube.com/watch?v=RxnV9Xcw914&t=24s) - This was used for creating the change of the colour of the navbar using intersection observers. Part two of three.
* [Intersection Observers - Fade into view](https://www.youtube.com/watch?v=huVJW23JHKQ) - This tutrial used for fading the about section into view and the products to slide in from left or right. Part three of three on intersection observers.
* Code Institute mini projects from the last module Full Stack Frameworks With Django helped me alot with this project. Both the blog project and the e-commerce in different parts of the code. When integrating stripe into this project I did it the same way as in the e-commerce mini-project, as an example.
### Media
* All the images of paintings are from the artist herself, Sandra Löwgren.
* The photos of the paintings were taken by Palli Kristmundsson.
* The background pictures from the page-intro are from unsplash and loads a random picture on every refresh of the page. The idea for using a background picture like this also came from the tutorial listed above, "Intersection Observers - Navbar". Source: unsplash.it/900

### Acknowledgements
* I want to thank my sister, Sandra Löwgren who has allowed me to create this project based on her paintings and helped me with her input on what would be relevant to display, what features that she prioritised based on her art. It's been great to create a project with a real purpose and get to create a website based on her needs.
* I want to thank my mentor greatly, Moosa Hassan for his help during this project and the last three that I made with the course from Code Institute. It was great support and feedback from him. In a project like this, when it's always possible to scale and build more funtionality, he helped me prioritize what to focus on which was exactly what I needed.
I received inspiration for this project from X