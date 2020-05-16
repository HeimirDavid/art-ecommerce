
# Sandra Löwgren Art Gallery and E-Commerce

SL Gallery is a Gallery and E-commerce where you can browse and buy original paintings or prints
from the artist Sandra Löwgren. There is also a blog/news section where you can keep up to date with the
latest from the artist!

Your Project's Name
One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.


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

* ***The paintings section*** is where all the paintings are. They are displayed with an image, name and a description, as well as if they are availible as original work, print or both. Here you can filter the paintings by which collection they belong to, with also information about the chosen collection.

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
* The **checkout** app takes care of the checkout process. This includes the providing forms the user needs, vilidating them and store the data in the userAddress and Order models in the app. Provide the correct error messages if something goes wrong, and rendering the correct templates.
* The **products** app takes care of all the paintings. In the models the product (painting) is stored with it's general info and three more tables which is more specific for the painting. This include the collection it belongs to, the original painting table with the size and price, along with a table for the prints with size and price. In the views.py file the functionallity of rendering all the products on one page is handled and categorising them by collection. As well as rendering a single product that is picked by the user.
* The home app takes care of rendering the index page and the two pages that I didn't want to create individual apps for. Those two are the contact page and the FAQ page since they are quite simple.
* The **newsposts** app is the most individual app of the site. The models is simple with one table. The views.py renderes all the articles, ordered by date and individual posts, picked by the user.
* The **orders** app renders the data from the Orders table from the checkout app, and displays it on a few different templates. It makes sure that only a superuser can access all the orders, and that a logged in user can access their own orders and see their status. This is all handled in the views.py file.

 ### Features Left to Implement

 * **Pagination** - at the moment the paintings are quite few and takes a long time to build up stock for. It would've been a good idea to implement it now but due to it not having the highest priority and the deadline coming closer, I choose to leave it for future implementation.
 * **Site owner input** - At the moment all the input of products, collections, prints and articles are input through the django admin panel. This works fine, but it would be more elegant for the owner of the site to have their own interface to interact with to input all of this data. Including changing the status of an order as well.
 * **Registered User Functionality** - allow a user to log in via their email and change their password.
 * **Address** - Since both the billing and shipping address is stored it would be great for an existing customer to be able to choose their previously used address from a dropdown when they go to the checkout.

Features Left to Implement
Another feature idea
## Technologies Used
* HTML, CSS, JS, Python where the core languages used to create this website.
* [Django 3.0.5](https://www.djangoproject.com/) - web framework.
* [Stripe](https://stripe.com/) - online payments platform. Their API used to validate and handle secure payments with credit card.
* [EmailJS](https://www.emailjs.com/) - Their JavaScript API used to send emails to the artist through the contact form.
* [Amazon Web Services](https://aws.amazon.com/) - AWS S3 Bucket for storing the media and static files.
* [Heroku](https://www.heroku.com/) - Hosting the live project
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Image library to handle the media upload.
* [Django forms bootstrap](https://pypi.org/project/django-forms-bootstrap/) - To format the django forms as bootstrap.
* [Fancybox](http://fancyapps.com/fancybox/3/) - Used to display the images as full view.
* [Bootstrap 4](https://getbootstrap.com/) - Used for their responsive css grid and basic styling for forms, buttons and tables.
*  [jQuery](https://jquery.com/) - For simplifying DOM manipulation
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - template language for Python
* [Lucidchart](https://www.lucidchart.com/) - To draw the Entity Relationship Diagram


### Databases
SQLite was used during development as it is Django's default database. PostgreSQL used for the deployed version and installed as an add-on in the Heroku dashboard for the application.
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
* [Entity-relationship diagram](https://github.com/HeimirDavid/art-ecommerce/blob/master/assets/erd/art-store-erd.png) - Here is the diagram over my database design. The cart and cart-item tables came a bit later as I had to go back to the drawing board when I switched to saving it in the database instead of using sessions. This was mainly due to the layout of the products and their variations. Every product has an original painting, but the prints and the original does not have the same prices. So every time a user adds a product to the cart, the product needs to be checked if it is a print or original and get the foreign key for it. Due to the fact that I had more experience with working with models in django I decided to design it this way instead of saving it all in sessions.


## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
* [Django Ecommerce Web application](https://www.youtube.com/watch?v=fhATkPoU22k&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK) - I found this tutorial playlist on youtube from the channel Coding Point. I used it to get inspiration and find soloutions for some of my problems with the cart, product variations and checkout. I built the base functionality for the carts app and part of the checkout app based on this series. Especially the views.py file in the carts app. Since it's over 80 clips I haven't looked through them all, just the ones that were a part about the cart and checkout. Episodes 22-33, 35-38 and 69-72.
* [Intersection Observers](https://www.youtube.com/watch?v=T8EYosX4NOo&t=291s) - After looking around for different simple soloutions to create some animations without using event listeners I found this tutorial on intersection observers. Part one of a three series tutorial.
* [Intersection Observers - Navbar](https://www.youtube.com/watch?v=RxnV9Xcw914&t=24s) - This was used for creating the change of the colour of the navbar using intersection observers. Part two of three.
* [Intersection Observers - Fade into view](https://www.youtube.com/watch?v=huVJW23JHKQ) - This tutrial used for fading the about section into view and the products to slide in from left or right. Part three of three on intersection observers.
* Code Institute mini projects from the last module Full Stack Frameworks With Django helped me alot with this project. Both the blog project and the e-commerce.
### Content
The text for section Y was copied from the Wikipedia article Z
### Media
* All the images of paintings are from the artist herseslf, Sandra Löwgren.
* The photos of the paintings were taken by Palli Kristmundsson.
* The background pictures from the page-intro are from unsplash and loads a randow pitcure on every refresh of the page The idea for using a background picture like this also came from the tutorial listed above, "Intersection Observers - Navbar". Source: unsplash.it/900.
The photos used in this site were obtained from ...

### Acknowledgements
* I want to thank my sister, Sandra Löwgren who has allowed me to create this project based on her paintings and helped me with her input on what would be relevant to display, what features that she prioritised based on her art. It's been great to create a project with a real purpose and get to create a website based on her needs.
* I want to thank my mentor greatly, Moosa Hassan for his help during this project and the last three that I made with the course from Code Institute. It was great support and feedback from him. In a project like this, when it's always possible to scale and build more funtionality, he helped me prioritize what to focus on which was exactly what I needed.
I received inspiration for this project from X