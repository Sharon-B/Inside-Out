# Testing

# Contents

# Code Validators

## CSS code was passed through Auto Prefixer to add vendor prefixes

* Prefixed by https://autoprefixer.github.io
* PostCSS: v8.3.6,
* Autoprefixer: v10.3.1
* Browsers: last 4 version

## CSS code was passed through the W3C CSS Validator 

base.css: No errors, 64 warnings relating to vendor prefixes.

profile.css: No errors, 4 warnings relating to vendor prefixes.

checkout.css: No errors, 18 warnings relating to vendor prefixes.

blog.css: No errors, 10 warnings relating to vendor prefixes.

## HTML code was passed through the W3C Markup Validator. 

No errors.

## Javascript code was passed through jshint. 

$ - undefined variable, this relates to jquery.

Stripe – undefined variable, this relates to using Stripe for payments.

## Python code was passed through PEP8 online. 

.py files passed through PEP8 online and returned All Right

# Lighthouse from Chrome Dev Tools Report

|                  | DESKTOP     |               |               |     | MOBILE      |               |               |     |
|------------------|-------------|---------------|---------------|-----|-------------|---------------|---------------|-----|
|                  | Performance | Accessibility | Best Practice | SEO | Performance | Accessibility | Best Practice | SEO |
| Home Page        | 85          | 98            | 100           | 90  | 64          | 96            | 100           | 92  |
| Products         | 95          | 98            | 100           | 100 | 72          | 96            | 100           | 100 |
| Product detail   | 92          | 92            | 100           | 100 | 70          | 90            | 100           | 100 |
| Add Product      | 97          | 99            | 100           | 100 | 84          | 97            | 100           | 100 |
| Edit Product     | 95          | 99            | 93            | 100 | 89          | 97            | 93            | 100 |
| Contact          | 98          | 100           | 100           | 100 | 82          | 98            | 100           | 100 |
| Profile          | 93          | 98            | 100           | 100 | 84          | 96            | 100           | 91  |
| Cart             | 97          | 94            | 100           | 100 | 68          | 92            | 100           | 100 |
| Blog             | 96          | 98            | 100           | 90  | 85          | 96            | 100           | 92  |
| Blog detail      | 97          | 98            | 93            | 100 | 79          | 96            | 100           | 100 |
| Add Blog         | 97          | 99            | 100           | 100 | 84          | 97            | 100           | 100 |
| Edit Blog        | 97          | 99            | 93            | 100 | 91          | 97            | 93            | 100 |
| Checkout         | 94          | 96            | 100           | 100 | 74          | 95            | 100           | 100 |
| Checkout Success | 97          | 100           | 100           | 100 | 76          | 98            | 100           | 100 |

# Responsiveness Testing

The responsiveness of the website was tested using Chrome Dev Tools and setting it to display on various mobile/tablet devices that are included. Responsiveness is optimised for screen sizes from 320px up.

# Device Testing

All aspects of the website mentioned below were manually tested on the following devices: iPad Pro, iPhone 8, MacBook Pro.

# Browser Testing

All aspects of the website mentioned above were manually tested on the following browsers: Chrome, Safari, Mozilla Firefox

# Friends And Family User Testing 

The general feedback was that the site looks well and is easy to navigate. They found the checkout process quick and easy to use. Devices used: iPad Pro, iPhone 8 Plus, Laptop (windows running the Chrome browser).

# Testing User Stories

## Testing New User Stories

1.	As a user I want a visually appealing site so that I will enjoy browsing for longer.

* Products are displayed in recipe cards for easy browsing, each card contains the basic information of an image, product name, price, to give the user an overview of the product.
* Professional look and a friendly feel to the website.
* Intuitive and easy to navigate around the site.
* Products are managed by an admin to ensure a high standard and continuity throughout.

2.	As a user I want to be able to register for an account so that I can have a profile.

* A user can register for an account via the Register link in the account icon dropdown menu.
* A user can easily register for an account by filling out their details on the form provided on the registration page.
* Once a user has registered they can login via the login page anytime they return to the site

3.	As a user I want a mobile friendly site so I can browse products while on my mobile.

* The site is responsive to ensure excellent user experience on all devices.
* The layout of each page is optimised for smaller devices to make it easy to read and navigate.
* Buttons are used consistently throughout the site which are easily recognisable and clickable for users on smaller devices.
* Back to top button is provided on long pages for enhanced user experience, especially on smaller devices.

4.	As a user I want to be able to contact the site owner so that I can ask any questions.

* A contact page is provided, so the user can quickly and easily send a message to the site owner.
* Once the message is submitted the user sees a message sent notification displayed on the screen, so they know the message has been sent.

5.	As a user I want to be able to view the site owners social media pages so that I can see what else they are doing.

* Social media links are provided in the footer of each page so the user can access them.
* The links are provided using instantly recognisable icons.
* Icons highlight on hover.

6.	As a user I want to be able to view my order total easily so I know how much I’m spending.

* Each time the user adds an item to their cart a running total of the cart is displayed at the top right hand corner of the screen under the shopping cart icon.

7.	As a user I want to know if there are any discounts available so I can make some savings while shopping.

* A banner across the bottom of the header element displays on all pages and here users will be able to see what offers, discounts are currently running on the site. At the moment free delivery is being offered for orders over €150.

8.	 As a user I want to be able to browse all products easily so that I can see what products are available.

* The user can shop all products via the Shop dropdown menu.
* The all products page displays all the products in an easy to browse layout.

9.	 As a user I want to be able to search for specific products so that I can easily find what I’m looking for.

* A search bar is provided in the page header of each page.
* The search bar allows users to search for terms that may appear in the products name or description.

10.	 As a user I want to be able to view products by category so I can easily browse for what I need.

* General categories provided in the Shop dropdown.
* On the top of the all products page there are clickable badges for each of the  seven product categories, which will display all products for that specific category, when clicked.

11.	As a user I want to be able to easily select the quantity of the product I want so I can be sure of what I’m buying.

* On the product detail page a quantity select box allows users to select the quantity they require.
* The product quantity can also be adjusted in the cart view page.

12.	As a user I want to be able to remove items from my shopping cart so I can change my mind about potential purchases.

* The user can easily update the items in their cart by adjusting the quantity and using the update link or the remove link.

13.	As a user I want to receive an order confirmation after checkout so I can be sure that my order was received.

* Confirmation notification on screen
* Order email confirmation
* Orders can also be checked from the order history section of a logged in users profile.

14.	 As a user I want to know that my actions have been acknowledged so I can be sure of what I’m doing.

* Notification messages are displayed for most user interactions.

    -	Logging in
    -	Registration
    -	Email registration verification
    -	Adding an item to the cart
    -	Making a purchase
    -	Email confirmation of purchase
    -	Adding a product/ blog/comment
    -	Deleting a product/blog/comment
    -	Editing a product/blog

15.	 As a user I want to be able to learn more about outdoor furniture and it’s use so that I can properly care for, maintain and design my outdoor space.

* A blog page is provided, where the site owner can publish articles providing tips on caring for outdoor furniture and planning, designing outdoor spaces of all sizes.
* The blog will be regularly maintained and added to in order to provide users with new inspiration for their outdoor space and to keep users returning to the site after making a purchase.
Each blog post also allows users to post comments about the content they are reading and the site owner will also regularly provide feedback here on users comments and encourage interaction with users.

16.	As a user I want to be able to easily view any new items that have been recently added to the store.

* On the home page there is a new arrivals section displaying the 3 most recently added products.
* There is also a button in this section with a call to action to view all new arrivals, which brings the user to a page displaying all the new arrivals
* In the Shop dropdown menu of the main navigation menu there is also a link to view all the new arrivals.
* All products that are categorised as new arrivals have a NEW badge on their product card and product detail page, so when browsing all products users can easily see which ones are new.

17.	As a user I want to have access to my order history and delivery info.

* A registration page is provided so users can register to have their own profile.
* Once a user has registered they can login via the login page anytime they return to the site.
* When a user makes a purchase they can save their delivery details to their profile so they don’t have to enter them every time they make a purchase ensuring ease of use for the user.
* A user can also update their delivery details on their user profile page.
* A user’s order history is also saved to their profile so they can check back on previous orders.

## Testing Registered User Stories

18.	As a registered user I want to be able to login easily to access my account information.

* Login page provides an easy and quick way for users to login.
* Once registered users only need to fill out their username or email and password in order to login.

19.	As a registered user I want to have my own profile where I can keep track of my orders and delivery info.

* Once a user logs in a profile is created for them.
* The users profile page is easily accessible from the user account  icon dropdown
* In the users profile page a user can update their delivery info.
* A users order history is also available in the users profile page so a user can view a list of all past orders and by clicking on the order number they can see that particular order. As a registered user I want to be able to see my order history so I know exactly what I have ordered

20.	As a registered user I want to be able to see my order history so I know exactly what I have ordered.

* A users order history can be viewed on the user profile page.
* A list of their order history is provided.
* If the user clicks on the order number for a particular order they can see that order in full so they know exactly what was ordered.

21.	As a registered user I want to have my details saved so I don’t have to enter them every time I make a purchase.

* Once a user checks out for the first time they have the option to save their details to their profile.
* Once a users details are saved in their profile they will automatically be filled out on the checkout page each time the user checks out.

22.	 As a registered user I want to be able to comment on a blog post so I can engage with other users and the site owner.

* A comment section is provided on each blog post page.
* Logged in users can comment on any blog post.
* If users are not logged in they are asked to log in or sign up in order to leave a comment.

## Testing Admin Superuser Stories

23.	As a superuser I want to be able to add/edit/delete any product so that I can maintain a well curated site.

* Superusers have access to a product management page via the my account icon dropdown menu.
* The product management page allows a superuser to add a product to the site.
* Superusers also have access to an edit link on all products either from the products pages or the product detail view and can edit any product via this link.
* Superusers also have access to a delete link on all products either from the products pages or the product detail view and can delete any product via this link.

24.	As a superuser I want to be able to edit/add/delete blog posts so that I can keep the site up to date on current trends.

* Superusers have access to a blog management page via the my account icon dropdown menu.
* The blog management page allows a superuser to add a blog post to the site.
* Superusers also have access to an edit link on all blog posts either from the blog page or the blog detail view and can edit any blog via this link.
* Superusers also have access to a delete link on all blog posts either from the blog page or the blog detail view and can delete any blog post via this link.

25.	As a superuser I want to be able to delete blog post comments so that I can keep the comments section well maintained.

* Superusers have access to a delete link for each comment left on a blog post and can delete any comment via this link.

## Testing Site Owner Stories

26.	As a site owner I want to provide a good user experience for my users, so that they want to come back.

* Professional look and a friendly feel to the website.
* Visually appealing throughout.
* Intuitive and easy to navigate around the site.
* Future releases to add more features to keep users interested and offer something new to returning users.

# Manual Testing

Each page was tested and passed under the criteria set out below.

## base.html

### Header

#### Logo:

* The logo is displayed in the header.
* Logo displays on all pages.
* The logo is a clickable link which returns the user to the home page.

#### Search bar:

* Displays on all pages.
* Search button highlights on hover.
* If a search term is entered the search results are displayed.
* If no search term is entered and the search button is clicked an error message appears saying no search term entered.
* Returns searches for terms found in the product name or description.
* If no search results are found for a search term ‘no results found’ is displayed.

#### My Account Icon Dropdown Menu:

* Displays on all pages
* For users who are not logged in the menu items are:

        Register, Log In

* For logged in users the menu items are:

        Profile, Log Out

* For superusers the menu items are:

        Product Management, Blog Management, Profile, Log Out

#### Shopping Cart Icon:

* Displays on all pages.
* If there is an item in the cart it changes color to blue.
* If there is an item in the cart it displays the current cart total under the icon.
* Each time an item is added to the cart the cart total is updated.
* Is a clickable link to the cart page.

#### Main Navigation:

* Displays on all pages.
* On mobile devices a collapsed menu is provided, on clicking the burger icon the navigation menu is revealed.
* On larger tablet devices and larger screen sizes the navigation menu items appear in the header.
* Each navigation menu item:
    * Highlights on hover
    * Is clickable
    * Links to the associated page
* For all users the navigation menu items are:

        Home, Shop, Blog, Contact

### Footer:

* Displays on all pages.
* Contains icons with links to social media pages.
* Each link brings users to the appropriate social media page.
* Icons highlight on hover.
* Social Media icons display on all pages.

## Home Page

### Hero Image:

* Displays a responsive hero image.

### New Arrivals Section:

* Displays a new arrivals section with product cards for the latest 3 new arrivals added to the database.
* Each product card contains a product image, Product name and product price. New arrivals also display a NEW badge on the product card.
* The product image on each product card is a clickable link.
* Clicking on the product Image brings the user to the full product detail page of the product clicked.

### Delete/ Edit Links:

* Only display on each product card if the current user is logged in as a superuser.
* Links highlight on hover.
* Edit link redirects the superuser to the Edit Product page.
* Delete link immediately deletes the product from the database and displays a Product deleted message to the user.

### View All New Arrivals Button:

* Brings users to view all products from the new arrivals category.

### Latest Blog Section:

* Displays the latest blog post added to the database.
* The blog post is displayed as a horizontal card with an image on the left and a blog title and some text, the author of the post and the date it was posted on the right.
* A read more button is provided, which brings the user to the full blog post page.
* The blog post image is also a clickable link which brings the user to the full blog post page.

### Delete/ Edit Links:

* Only display on each blog post card if the current user is logged in as a superuser.
* Links highlight on hover.
* Edit link redirects the superuser to the Edit Blog page.
* Delete link immediately deletes the blog from the database and displays a Blog deleted message to the user.

### Check Out All Our Blog Posts Button:

* Brings users to view the blog page.

## Products Page

* Displays product cards for all products from the database.

### Product Cards:

* Each product card contains a product image, Product name and product price. New arrivals also display a NEW badge on the product card.
* The product image is a clickable link which brings the user to the full product detail page of the product clicked.

### Category Badges:

* Category badges are displayed for each category.
* Clicking on a category badge lets the user view products from that category.

### Product Sorting:

* Product sorting is available via a Sort dropdown. Products can be sorted by:

    * Category a-z
    * Category z-a
    * Price high - low
    * Price low – high
    * Product Name a-z
    * Product Name z-a

### Product Count:

* Product count is provided at the top of the page, product count adjusts accordingly depending on whether viewing all products or a product category.

### All Products Link:

* Links to the all products page.

### Delete/ Edit Links:

* Display on each product card if the current user is logged in as a superuser.
* Links highlight on hover.
* Edit link redirects the superuser to the Edit Product page.
* Delete link immediately deletes the product from the database and displays a Product deleted message to the user.

### Back To Top Button:

* Displays at the bottom right corner of the page.
* Highlights on hover.
* Clicking on it brings the user to the top of the page

## Full Product Detail Page

*   Displays for all users.
*   Displays the full product detail on the page.
*   Displays the product name, product image, product category, product description, if it is a product from the new arrivals category a NEW badge is also displayed.

### Quantity Select Box:

*   Allows the user select the quantity of the product that they would like to purchase.
*   The quantity can either be typed in or adjusted using the +/- buttons.
*   The quantity is limited to a number between 1 and 99.

### Continue Shopping Button:

*   Continue shopping button brings users back to the all products page.

### Add To Cart Button:

*   Add to cart button adds the selected quantity of the item to the cart.
* Displays a success toast message to alert the user that the product has been added to the cart, the success toast message also contains an overview of the current cart contents, a view cart button and a check out button.
* The message disappears after 5 seconds.

### Delete/ Edit Links:

* Display on each product card if the current user is logged in as a superuser.
* Links highlight on hover.
* Edit link redirects the superuser to the Edit Product page.
* Delete link immediately deletes the product from the database and displays a Product deleted message to the user.

## Add Product Page

* Only available to superusers
* Allows a superuser to add a new product to the site, by filling out a form with the fields:
    * Category
    * Product name
    * Product description
    * Product number
    * Product price
    * Product Image

### Add Product Button:

* Highlights on hover.
* Submits the product to the database.
* Form only submits if valid.
* Displays a message letting the user know that the item was added to the database.

### Cancel Button:

* Highlights on hover.
* Returns the user to the products page.

## Edit Product Page

* Similar to the add product page but the fields are pre-populated with the existing product info.

## Cart Page

* Displays a list of the products in the cart in a table/grid format.
* Displays the subtotal of each item in the cart depending on the quantity of that item.
* Allows the user to adjust the quantity of an item in the cart using the quantity select box for each item.
* Cart total, delivery charges and grand total are displayed at the bottom of the page
* If the cart total is less than the €150 free delivery threshold a reminder to the user is displayed telling them how much more they need to spend to get free delivery.

### Quantity Select Box:
* Displays for each item in the cart.
* Allows the user to adjust the quantity of the product that they would like to purchase.
* The quantity is limited to a number between 1 and 99.
* Once the quantity is set the update link will update the quantity in the cart for that item and its subtotal. A quantity updated notification message will also appear.
* The remove link will remove the item entirely from the cart. A Item removed notification message will also appear.

### Continue Shopping/ Checkout Buttons:

* Highlight on hover.
* Continue shopping button returns the user to the products page.
* Checkout button brings the user to the checkout page.

## Checkout Page

* Displays an order summary, with the items to be purchased, their quantity and subtotal for each item.
* Displays the order total, delivery and grand total.
* Displays a form for the user to enter their details, delivery info and payment details.
* Logged in users have the option to save their payment details to their profile, once this box is checked their payment details are saved to their profile and the form will be prepopulated the next time they make a purchase.
* Users who are not logged in are advised to register and or login in order to save their details.
* The amount to be charged to the card is displayed under the checkout button.

### Update Cart/ Checkout Buttons:

* Highlight on hover.
* Update cart button returns the user to the shopping cart page.
* Checkout button submits the checkout form.
* Once the form is valid the order is processed.
* If the form is not valid users are advised to check the form for errors.
* Once the payment is processed successfully a checkout success page is displayed with an overview of the order.
* Once the payment is confirmed a confirmation email is sent.
* For logged in users the order is saved to their order history which can be viewed from their profile page.

## Checkout Success Page:

* Displays an overview of the order.
* Initially displays a message notification confirming the order.
* Lets the user know that a confirmation email will be sent to the email address they used.

### Checkout New Arrivals Button:

* Displays after the order summary.
* Highlights on hover.
* Brings users to view the new arrivals category of products.

## User Profile Page

* Displays for a logged in user.
* Provides a form where the user can update their details.
* If a user has already saved their details the form will be pre-populated.
* Displays  the order history for that user.
* The order number for each order in the order can be clicked to view the full order.

### Update Details Button:
* Displays at the bottom of the users details form.
* Highlights on hover.
* Updates the users’ details.

## Blog Page
* Displays all blog posts.
* Each blog post is displayed as a horizontal card with an image on the left and a blog title, some text, the author of the post and the date it was posted on the right.
* A read more button is provided, which brings the user to the full blog post page.
* The blog post image is also a clickable link which brings the user to the full blog post page.

### Delete/ Edit Links:

* Only display on each blog post card if the current user is logged in as a superuser.
* Links highlight on hover.
* Edit link redirects the superuser to the Edit Blog page.
* Delete link immediately deletes the blog from the database and displays a Blog deleted message to the user.

### Back To Top Button:

* Displays at the bottom right corner of the page.
* Highlights on hover.
* Clicking on it brings the user to the top of the page.

## Blog Detail Page 

* Displays the full blog post article.
* Displays the Blog post title, image, article and the author and date it was posted.

### Comments

* Comments can be read by all users.
* Logged in users can leave a comment by filling in the comment form and clicking Add Comment
* Comment form only submits if valid.
* Users who are not logged in are advised to register or login to leave a comment.
* A superuser can delete a comment via a delete link that displays for them.

### Add Comment Button:

* Submits the comment form.
* Displays a notification message saying the comment was successfully added.

### Back To Top Button:

* Displays at the bottom right corner of the page.
* Highlights on hover.
* Clicking on it brings the user to the top of the page.

## Add Blog Page

* Only available to superusers
* Allows a superuser to add a new blog post to the site, by filling out a form with the fields:
    * Blog Title
    * Blog body text
    * Blog Image

### Add Blog Button:

* Submits the blog post to the database.
* Only submits if the form is valid.
* Displays a message letting the user know that the blog post was added to the database.

### Cancel Button:

* Returns the user to the blog page.

## Edit Blog Page

* Similar to the add blog page but the fields are pre-populated with the existing blog post info.

## Contact Page

* Displays for all users.
* Displays a contact form.
* Users must fill out all fields in the form.
* Form only submits if valid.

### Send Message Button:

* Highlights on hover.
* Form does not submit if fields are left empty.
* Submits the form and displays a notification message ‘Message sent”

## 404 Page

* Displays when a 404 - page not found error is encountered.
* Tells the user that the page could not be found.
* Provides a return home button.

### Return Home Button:

* Highlights on hover.
* Returns the user to the home page.

## 500 Page
* Displays when a 500 – internal server error is encountered.
* Tells the user that there’s an internal server error.
* Provides a return home button.

### Return Home Button:

* Highlights on hover.
* Returns the user to the home page.


