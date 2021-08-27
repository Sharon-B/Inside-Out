# Inside Out Outdoor Furniture

![Responsive Image]( "Am I Responsive")

[Link to Live Project]()

# Project Summary

Inside Out Garden Furniture is an e-commerce store where users can browse and purchase garden furniture items from various categories. 

# Contents


# User Experience 

# Strategy

## Developer Objectives

To grow my skills as a developer and create a simple easy to use site. Develop the project from its initial concept to the final finished product. To demonstrate my skills of Python and Django. The project will further my knowledge of Python, the Django framework, Django templating language, HTML, CSS, Javascript and the use of databases and their implementation.

### Target Audience

*   People looking for inspiration for their gardens
*   General public

## User Stories

### New User Stories

1. As a user I want a visually appealing site so that I will enjoy browsing for longer.
2. As a user I want to be able to register for an account so that I can have a profile.
3. As a user I want a mobile friendly site so I can browse products while on my mobile.
4. As a user I want to be able to contact the site owner so that I can ask any questions.
5. As a user I want to be able to view the site owners social media pages so that I can see what else they are doing.
6. As a user I want to be able to view my order total easily so I know how much I’m spending.
7. As a user I want to know if there are any discounts available so I can make some savings while shopping.
8. As a user I want to be able to browse all products easily so that I can see what products are available.
9. As a user I want to be able to search for specific products so that I can easily find what I’m looking for.
10. As a user I want to be able to view products by category so I can easily browse for what I need.
11.	As a user I want to be able to easily select the quantity of the product I want so I can be sure of what I’m buying.
12.	As a user I want to be able to remove items from my shopping cart so I can change my mind about potential purchases.
13.	As a user I want to receive an order confirmation after checkout so I can be sure that my order was received.
14.	As a user I want to know that my actions have been acknowledged so I can be sure I am doing the right thing eg add an item to the cart.

### Registered User Stories

15.	As a registered user I want to be able to login easily to access my account information.
16.	As a registered user I want to have my own profile where I can keep track of my orders and delivery info.
17.	As a registered user I want to be able to see my order history so I know exactly what I have ordered
18.	As a registered user I want to have my details saved so I don’t have to enter them every time i make a purchase.

### Admin User Stories

19.	As a superuser I want to be able to add/edit/delete any product so that I can maintain a well curated site.
20.	As a superuser I want to be able to add/edit/delete blog posts so that I can keep the site up to date on current trends.
21.	As a superuser I want to be able to delete blog post comments so that I can keep the comments section well maintained.

### Site Owner Stories

22.	As a site owner I want to provide a good user experience for my users, so that they want to come back.

# Scope

This will be a Minimal Viable Product containing the most essential core content required.

## Functional Specifications 

*   Home
*   Search functionality
*   All Products
    * Products by category
*   Product Detail
*   Shopping cart functionality
    *   Add to cart
    *   Remove from cart
    *   Update cart
*   Checkout functionality
    *   Checkout success
*   Stripe payments
*   Contact
*   Registration
*   Log In
*   User Profile functionality:
    *   Create a profile
    *   Save delivery info
    *   View order history
*   Log out functionality
*   Blog
*   Admin functionality:
    *   Manage Products – Add, edit & delete products
    *   Manage Blog – Add, edit & delete blog posts
    *   Manage blog comments – delete
*   Notifications

## Content Requirements

*   Logo
*   Main Navigation
*   Search bar in header
*   User account dropdown in header
    *   Register/Login/out/profile access
*   Cart icon in header
*   Home page
    *   Hero image
    *   New arrivals section
    *   Latest blog post section
*   All Products page with image and price
    *   View by category options
*   Product detail page
*   Shopping cart page
    *   Users can add items to the shopping cart
    *   Users can select the quantity of items to add
    *   Users can remove items from the shopping cart
*   Checkout Page for processing payments
    *   Checkout success page
*   Register page with registration form & link to Log In page
*   Log In page with login form & link to Registration page
*   Contact Us page
*   User profile page
    *   Users delivery details
    *   Users order history
*   Blog page
*   Blog detail page, with comments section
*   Admin pages navigation – in user account dropdown
*   Admin manage products page – add/edit/delete any product
    *   Add product page with form for adding new product details
    *   Edit product page with form for editing product details
    *   Delete product functionality
*   Admin manage blog page - add/edit/delete blog posts
    *   Add blog page with form for adding a new blog post
    *   Edit blog page with form for editing blog posts
    *   Delete blog post functionality
*   Footer with Social media links

# Structure

## Interaction Design 

User interactions will be intuitive and consistent throughout the site to ensure it is easy to use and quick to learn for the user. Clickable links and buttons are used throughout the site to offer the user easy access to pages. They will have a hover effect applied so they are easily identifiable when a user hovers over them. A cursor pointer will appear when hovering over clickable images.

Toast notifications have been used throughout the site to offer the user feedback on their actions for example when adding an item to the cart a success notification will be displayed advising the user that the item has been added to the cart.

## Information Design 

Will allow for the prioritisation of information to be displayed in a clear and concise manner to make it as easy as possible for the user to read and quickly find the information that is most relevant to their needs.

# Skeleton

## Wireframes



## Difference between final design and original wireframes





# Surface

## Typography

PlayFair Display is used for the logo and headings throughout the site as it is well suited for titling and suits the style of the site.

Source Sans Pro is used for all other text content. It is a sans serif typeface that works well in this context and is easily readable.

## Colour scheme

### Logo



The logo uses two colours blue #0E5CA5 and green #097485, both used due to their association with the outdoors and nature which is appropriate for the theme of this site.

### Rest Of Site

1. Primary Colour - The same blue #0E5CA5 used in the logo was then used as the base for the color of the rest of the site.

- Headings 
- Borders 
- Dark background button

2. Secondary Colour - An accent light blue #B2CAD8 was also derived from the same blue by reducing the lightness of the original blue.

- Banner background
- Form fieldset background
- Light background button
- Footer background

3. Background Colour - A light background colour #F6F6F6 was chosen as it worked well with the blue theme providing contrast and it emphasised the products by not making the site too busy.

- Main background
- Text on dark button
- Background on no background button

4. Text Color #2D3636

- Text
- Icons

5. Alert Colors and Alert Text

*   Success #097485
    -   Success Toast Messages

*   Info #0E5CA5
    -   Info Toast Messages
    -   Info Text
    -   Edit and Update links

*   Error #AE093E
    -   Error Toast Messages
    -   Delete and Remove links
    -   Error text

*   Warning #875531
    -   Warning Toast Messages

6. Buttons 

- No background
- Light background
- Dark background

# Features 

*   Responsive
*   Logo
*   Navigation in header which collapses for mobile use
*   Search
*   All products displayed with product image, name and price to display each product for browsing
*   Product image on card is a clickable link to the product detail view
*   Home page features new arrivals section
*   Home Page features latest blog post section
*   Hero image on home page
*   Back to top button
*   Shopping cart
*   Checkout functionality with checkout success page when complete
*   Payments method using Stripe
*   Forms for adding and editing a product, blog post
*   Single product detail view page
*   Single blog post detail view page with comments section
*   Contact page
*   Registration page
*   Log in page
*   Log out functionality
*   User profile
*   User order history
*   User can save delivery details in their profile
*   Form validation
*   Highlight buttons on hover
*   Highlight links on hover
*   Footer with social media links
*   No Delivery charge for orders over €150
*   Notification alerts

## Future Features

*   Confirm delete
*   Add reviews app to enable users to leave reviews for products.
*   Allow users to login via their social media accounts
*   Save shopping cart items for later
*   Discount code

# Technologies Used

[Python](https://www.python.org) - Main language used for programming the app.

[Django](https://www.djangoproject.com) - Framework used.

[Html](https://www.w3schools.com/html/html_intro.asp) - Hyper Text Markup Language, used for creating the website.

[Css](https://www.w3schools.com/css/) - Cascading Style Sheet, used for styling the website.

[Javascript](https://www.javascript.com) – Used for providing javascript functionality to the site

[Stripe](https://stripe.com/) - Used for adding payment functionality.

[AWS](https://aws.amazon.com/) - Used for hosting static and media files.

[Bootstrap 5](https://getbootstrap.com) - Bootstrap grid system, utility classes, nav-bar, toasts, cards.

[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for rendering forms.

[crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5) - Used to facilitate using crispy forms with bootstrap 5.

[Google Fonts](https://fonts.google.com) - The 2 fonts used throughout the website are from Google fonts.

[Fontawesome](https://fontawesome.com/) - Used for icons.

[Balsamiq](https://balsamiq.com) – Used for creating the wireframes.

[Git](https://git-scm.com/) - Used for version control.

[GitHub](https://github.com) - Used to store the project repository.

[Gitpod IDE](https://www.gitpod.io/) - Development environment where the site was built.

[Heroku](https://signup.heroku.com/) - Where the live site is deployed.

[Gimp 2.1](https://www.gimp.org/) - Used for editing, scaling images.

[favicon.io](https://favicon.io/favicon-generator/) - Used for creating a favicon.

[Tiny png](https://tinypng.com) - Used for compressing images.

[Webaim contrast checker](https://webaim.org/resources/contrastchecker/) - Used to check the contrast between the text font and background colours.

[Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) - Used throughout the development of the website to quickly see changes, find problems and debug. Also used to view website in different device views.

[Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Dev Tools - Used for site performance review.

[AutoPrefixer](https://autoprefixer.github.io/) - Used to add vendor prefixes onto the CSS code to ensure compatibility with various browsers.

[W3C HTML validator](https://validator.w3.org/) - Used to validate code.

[W3C CSS validator](https://jigsaw.w3.org/css-validator/) - Used to validate code.

[JSHint](https://jshint.com/) – Used to validate Javascript code

[Coolors](https://coolors.co/) - Used for selecting complimentary colour palettes.

[GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) - Used for creating a table of contents in README.md

# Implementation 

Once the initial concept for the project was decided upon I first developed the wireframes. From these wireframes I then developed the basic database structure required.

I then set up the Django framework first by installing Django using:

        pip3 install django

Then I created the project using: 

        django-admin startproject inside-out

I checked the .gitignore file which is automatically created when using the Code Institute template and ensured the following files were added:

        *.sqlite3, *.pyc, __pycache__ and env.py

The environment variables needed to run the project were saved in env.py. I ran the initial migrations using 

        python3 manage.py migrate

I created a superuser using the command:

        python3 manage.py createsuperuser

At this point it is possible to run the server for the first time and check that Django has been installed.

        python3 manage.py runserver

I created requirements.txt for all the dependencies used. I set up a base.html from which my html templates would be extended from. 
The site consists of 7 apps – blog, cart, checkout, contact, home, products and user_profiles. Each app was created using the command 

        python3 manage.py startapp <app_name>

As I added a new app I added it to the list of installed apps and set up its models and register them in the admin.py. Then I would create the initial view which would usually be added to as more functionality was added to the site, add its url path in urls.py and include the url path in the projects main urls.py file. Add forms in forms.py (if needed), and any associated html templates. Django templating language was used to insert the data into the html templates.

## Issues/Solutions

The Stripe card input field was not displaying, after researching why this could be and contacting tutor support I realised it was because I changed some of the styles in the stripe_elements.js file, which were originally from the Stripe website. Once I reverted these styles back to how they were I could then see the Stripe card input, it was as if the changes I made overlapped the original Stripe card input field. I also changed some of the Stripe styling units in checkout.css from px to rem to keep it inline with the rest of the project, this resulted in a warning in the console so I reset them back to px.

Due to a Gitpod issue my Gitpod workspace got stuck in 'building' mode and could not be opened, after much back and forth with Gitpod I had to start a new workspace using the green gitpod button from the GitHub repo. Having started the new workspace I had to re-install all requirements - I could do this using the command `pip3 install -r requirements.txt`, create a new superuser, run all migrations again, and set up my env.py file again. I also had to rebuild the database.

While initially testing the save-info checkbox in the checkout page during development I noticed that even with the save-info box unchecked it was saving the user's delivery details to the user profile over-writing any details that were already saved in the users' profile. While looking into this I found a Slack post by @Philipp which helped me to resolve this issue. In stripe_elements.js where its getting the form data I changed 

    let saveInfo = Boolean($('#id-save-info').attr('checked'));

to

    let saveInfo = $('#id-save-info').is(':checked');

This seems to give a better True/False result for whether the checkbox is checked and whether the data should be saved or not. Then within the webhook_handler.py I changed 

    if save-info:

to 

    if save-info is True:

I was also having another issue where the info being saved to the users profile was being displayed as a tuple instead of a string. Once I made the above changes this issue was also resolved, so needed no further investigation.

After completing the delete_comment() view to delete a comment made on a blog post I was getting a Django 404 error - page not found. No BlogPost matches the given query. This was because I originally had my delete comment url path set to 

    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

which was very similar to the url path for delete_blog_post, so django wasn't making it past the delete blog post url path to get to the delete comment url path. By changing the delete comment url path to 

    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

the issue was resolved.

## Known Bugs



# Defensive Design



# Testing

Testing documentation can be found [here]()



# Deployment





# Credits

## Code


## Resources



## Content


## Media


  

## Acknowledgements

My mentor @spence_mentor for great support and positivity throughout.

All at Code Institute and Tutor support.

The Slack Community for their ever present knowledge.

##  Disclaimer

This project is for educational purposes only.