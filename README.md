[![Build Status](https://travis-ci.org/elg1e/elg1e-Vintage.svg?branch=master)](https://travis-ci.org/elg1e/elg1e-Vintage)

![Vintage Logo](https://github.com/elg1e/elg1e-Vintage/blob/master/static/images/VintageText.jpg)

Vintage is an ecommerce web application which allows users to shop, search, bid and purchase vintage artifacts. The aim is to allow users to go online and navigate the easy to use website to discover their most desired vintage artifacts. 

Users simply search for artifacts they wish to learn about or purchase. If they see something they desire or want to keep and eye on they can create an account and either place a bid using the original auction-style system or buy an item instantly with the 'Buy It Now' button.

## Table of Contents

1. [**UX**](#ux)
    - [**User Stories**](##UserStories)
    - [**Wireframes Mockups**](##wireframesmockups)
2. [Features](#features)
    - [**Navigation**](##Navigation)
    - [**Homepage**](##Homepage)
    - [**Shopping Cart**](##Shoppingcart)

# UX

This project is aimed at all generations fascinated by the ancient world. The website is clean and simple allowing users to discover artifacts, learn about their history and purchase the items using the easy to follow bidding system or buy it now option. The simplistic navigation bar allows for a seamless transition between pages and the muted colour scheme creates an appealing platform for the artifacts to shine.

## User Stories

* As a user, I would like the website to be responsive with all of my devices.
* As a user, I would like to search for my ideal item so that I can narrow down my search faster.
* As a user, I would like to store items while I look for something else I'd like to purchase, then go back and purchase everything together.
* As a user, I would like to try and bid on an item to try and purchase for a low price.
* As a user, I would like to find an item I like and purchase straight away without bidding.
* As a user, I would like to be able to press a button to help me if I've lost my password. I would then like a email confirmation to give me my new password setup. 
* As a user, I would like to find what I'm looking for fast, by simply pressing one button to get to a list of items I wish to purchase.

## Wireframes Mockups

 Below there are images of my initial ideas/mock-ups of the website:

* Mockup images of the website:

![Wireframe1](https://github.com/elg1e/elg1e-Vintage/blob/master/static/images/vintageWireframe1.jpg)
![Wireframe2](https://github.com/elg1e/elg1e-Vintage/blob/master/static/images/vintageWireframe2.jpg)

# Features

## Navigation

 The navigation bar is simplistic and responsive for all devices. The navigation bar in mobile resolutions is fixed to the top of the screen, making it simple and easy for mobile users to move quickly around the site.

## Homepage

 The Homepage in mobile resolution consists of a title, search bar, links to each section of the site, navigation bar and sign in/register links. By pressing the title it will hyperlink you back to the homepage for easy access. The search bar is to search for a specific item.
The sign in or register links are to sign up to the website which will allow you to bid and buy out items, add items to your cart or check your bidding progress.

 The Homepage in desktop resolution will still have all of the above but the navigation bar will be different to the mobile resolution due to having more space for extra description. 

## Shopping Cart

 The Shopping Cart is the same as most ecommerce websites. The user can click an item they wish to purchase and this item will enter their cart. When checking out the users items will be in there ready for purchase.

## Bidding/Buying Out

 The Bidding and Buying out system is designed to allow users to out bid eachother on items they wish to purchase. The items will also have a buy out price, so if they wish to buy the items instantaniously to avoid missing
out they can do so with this function.

### Future features

 One of the future features that could be implemented into the website is real time expires for the user bidding system. The website currently does not have a system that when web team add 
a new product onto the site, the expiry time does not exist. By adding a expiry time/date the user can only create bids on items until the time runs out. Once the time expires the items would disapear 
from the users view, stopping any further bids and making the last highest bidder the winner of the item.

# Technologies Used

* [HTML](https://en.wikipedia.org/wiki/HTML) Mark-up language used for creating the website.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) Stylesheet language used to create the presentation of the website.
* [JS](https://www.javascript.com/) Is a high-level, just-in-time compiled, object-oriented programming language.
* [JQuery](https://jquery.com/) Used to simplify some of the DOM manipulations.
* [Python](https://www.python.org/) Is an interpreted, high-level, general-purpose programming language.
* [Django](https://www.djangoproject.com/) Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern.
* [Travis](https://travis-ci.org/) Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.
* [Heroku](https://www.heroku.com/) Is a cloud platform as a service supporting several programming languages.
* [Bootstrap](https://getbootstrap.com/) Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
* [FontAwesome](https://fontawesome.com/) Font Awesome is a font and icon toolkit based on CSS and LESS. 
* [Stripe](https://stripe.com/gb) Stripe API is a payment processing platform.
* [GitHub](https://github.com/) Is website that provides hosting for software development.
* [Hover.css](https://ianlunn.github.io/Hover/) Is a GitHub repository which was made for creating hover effects.

# Testing

## Homepage Testing

### Navigation Testing

#### Register

1. Click on the Register link.
2. When register page opens follow the steps titled Create a new account.
3. When you have typed the details required, press the create account button.
4. This will bring you back to the homepage with pop up information to inform the user the account has been created.

1. Click on the Register link.
2. Enter the requirements for creating an account except from Username.
3. There will be a pop up informing you that you must enter this field.
4. Repeat this sequence for each requirement.
5. By entering the same username as before you will also be unable to complete the Register form.

1. Click on the Register link.
2. Press Sign in button.
3. Sends you to the login page.

#### login/logout

1. Click on the Login link.
2. Enter your username and password.
3. Press the Login button.
4. You will be forwarded to the homepage with a pop up informing you that you are now logged in.
5. Click Logout buton.
6. You will see a pop up informing you that you are now logged out.

1. Click on the Login link.
2. Enter your username but not your password.
3. You will be asked to complete the fields.
4. Repeat this for username and password.

1. Click on the Login link.
2. Press Forgot my password.
3. Forgotten password page will appear.
4. Enter your email.
5. Press Reset Password.
6. Page will appear informing you that you will recieve an email.
7. Follow the steps in the email.

#### Artifacts

1. Click on the Artifacts link.
2. This will send you to the Artifacts page.

1. Click one of the homescreen artifact images.
2. This will send you to the product page.

#### Cart

1. Click on the Cart link.
2. This will send you to the cart page.

#### Search Bar/button

1. click inside of the search bar.
2. Search for a specific product.
3. Press the search button or press enter.

## Artifact Page

#### Bidding

1. Type in the bid area and enter a higher bid than the current bid.
2. Press the bid button.
3. Pop up will appear informing you that you are the highest bidder.

1. Repeat this without being signed in.
2. You will be unable to enter a bid and you will be sent to the login page.

1. Type in the bid area and enter a lower bid than the current bid.
2. Press the bid button.
3. Pop up will appear informing you that you must bid higher than the current bid.

#### Buyout

1. Click the Buyout button.
2. The item will be added to your cart.
3. You will then be sent to the cart page.
4. Press checkout.
5. Follow the instructions for payment.
6. Press the Submit Payment button.

## Known Issues

During development, I encountered an issue with the password reset feature. Pressing the Display Unlock Captcha button allowed me to send the emails through for a short period of time. However, after a certain period the Display Unlock Captcha seemed to reset and I would have to reauthorise the website.
After speaking with technical support, they highlighted the known issue with Django SMTP with Gmail. 

# Responsive Design

 The website has been tested using the developer tools and also with [Am i Responsive](http://ami.responsivedesign.is/). This was done so that the website will be compatible in all different screen sizes.

 The website has been tested in the following device resolutions:

 ![Responsive Vintage](https://github.com/elg1e/elg1e-Vintage/blob/master/static/images/vintage-responsive.png)

## Mobiles

* Moto G4
* Galaxy S5
* Pixel 2/XL
* iPhone 5/SE/6/7/8
* iPhone 6/7/8+
* iPhone X
* Galaxy S5/S9/S9+
* Tablets
* iPad/iPad Pro
* Surface Duo
* Galaxy Fold
* Desktops/XL Desktops

 The website has been tested with these browsers:

* Google Chrome
* FireFox
* Internet Explorer
* Microsoft Edge

# Validation

 The website has be validated using:

* HTML: [W3C Markup Validation Service](https://validator.w3.org/)
* CSS: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* Jhint: [Javascript Code Quality Tool](https://jshint.com/)
* Python: [pep8online](http://pep8online.com/)

# Deployment

 The live website was deployed using Heroku. The site can be found [here:](https://vintage-fullstack.herokuapp.com/)

 My repository can be found [here:](https://elg1e.github.io/elg1e-Vintage/)

 To create the website, I have used the coding platform Gitpod. Deployment and source control was done via GitHub and Heroku. To recreate this repository locally you must have the following installed:

 * [python3](https://www.python.org/)To run the application
 * [PIP](https://pypi.org/project/pip/)To install the requirements.
 * [Git](https://www.atlassian.com/git/tutorials/install-git)For the cloning and version control.
 * [GitPod](https://www.gitpod.io/)For the workspace used to develop the project (Another IDE could be used).

 The next steps for cloning this project from [github](https://github.com/) are:

 1. Go to GitHub then, navigate to the main page of the repository.
 2. Above the list of files, click the button named Code.
 3. To clone the repository click the copy button next to the HTTPS.
 4. Open your terminal window, inside type git clone and paste the HTTPS.
 5. Press enter to create your local clone.

 To finalise, you will need to create an env.py with your own environment variables, Then, install all the requirements from the [requirements.txt](https://github.com/elg1e/elg1e-Vintage/blob/master/requirements.txt).

Follow these steps for remote deployment using Heroku:

* Firstly, log into Heroku and created a new application.
* Then, follow the steps Heroku give you on the website to connect Heroku to the web app. These steps are to install the Heroku CLI by logging in.
* After this, create a new GitHub repository.
* Once this is complete deploy the application by commiting and pushing the work via git push heroku master branch.
* Before pushing anything to Heroku you must have a requirements.txt file and a Procfile.
* Then, by typing in the terminal: heroku ps:scale web=1 this will then get the Heroku app up and running.
* Finally, open up the Heroku app settings on the Heroku website and make sure to set the config variables (IP/PORT).

# Credits

## Content

The description for each of the images on the website was taken from [wikipedia](https://www.wikipedia.org/), [Ancient Origins](https://www.ancient-origins.net/artifacts-other-artifacts/ten-amazing-artifacts-ancient-world-002105) and [iwm](https://www.iwm.org.uk/history/8-peculiar-battle-trophies-taken-from-the-front)

## Media

The images used in this site were obtained from:

* [The Holy Grail Image](https://www.history.com/news/is-the-quest-for-the-holy-grail-over)
* [The Knight Image](https://historydaily.org/amazing-historical-artifacts)
* [The Tutankhamun Image](https://www.timetrips.co.uk/ep-tutmask.htm)
* [The Image of Agamemnon](https://www.oddee.com/list/10-incredible-historical-artifacts/)
* [Thor's Hammer](https://www.ancient-origins.net/artifacts-other-artifacts/ten-amazing-artifacts-ancient-world-002105)
* [Antikythera Mechanism](https://www.vox.com/science-and-health/2017/5/17/15646450/antikythera-mechanism-greek-computer-astronomy-google-doodle)
* [Nefertiti Bust](https://en.wikipedia.org/wiki/Nefertiti_Bust)
* [Trench Dagger](https://www.iwm.org.uk/history/8-peculiar-battle-trophies-taken-from-the-front)
* [Cavalry Bugle](https://www.iwm.org.uk/history/8-peculiar-battle-trophies-taken-from-the-front)
* [SpartanLogo](https://st2.depositphotos.com/2527057/10398/v/450/depositphotos_103986174-stock-illustration-spartan-helmet-sign.jpg)