<h1>The BookShelf Chair</h1>
<br>
<br>
The BookShelf Chair is an online book store which also provides a book club to discuss and interact with other readers<br>
Users can purchase books or leave a comment for a book<br> 
They can create an account to keep track of their orders and they can also subscribe to a mailing list.<br>
<br>
<img src="media/am_i_responsive.jpg" alt="multiple screen sizes diplaying the website">
<br>
<br>
<h2>User stories</h2>
The project has started by establishing the user stories based on the template: As a "site user" I can "action" so that "reward"<br>
The steps followed to create the user stories in Github can be seen below:<br>
1. In the project repository, from the main menu, select Issues<br>
2. Select New Issue from the right-hand side and add a title, starting with USER Stories.<br>
3. Add a description in the Description box, based on the template above.<br>
4. Submit the new issue.
<br>
<img src="media/userstories.jpg" alt="using github issues to create a board">
<br>
There are a total of 21 User Stories for this project, as listed below:<br>
- View list of products<br>
- View individual product details<br>
- Add comment to Book Club Page<br>
- Add New topic to Book Club page<br>
- Register for an account<br>
- Login/Logout page<br>
- Article/post view<br>
- Email confirmation after registering<br>
- Change password<br>
- Sort list of products<br>
- Sort products by category<br>
- Search by name or description<br>
- Add product in shopping bag<br>
- See total of bag content<br>
- See subtotal after each purchase<br>
- Pay securely<br>
- Add new products as a site owner<br>
- Edit products as a site owner<br>
- Delete products as a site owner<br>
<br>
<br>
<h2>Features</h2>
<hr>
<h3>Existing Features</h3>
<br>
Creating an admin in Django to manage the page<br>
<img src="media/admin_site.jpg" alt="admin page to manage a website">
<br>
Creating a product page with all categories available, with filter option to sort them.<br>
<br>
<img src="media/book_page.jpg" alt="book page">
<br>
Creating a Book Club page to share comments and join conversations. Each topic has a link field to add the link to a certain book from the store<br>
<br>
<br>
<img src="media/book_club_page.jpg" alt="admin page to manage a website">
<br>
A My account page to login/register and see the history og a sale and delivery details.<br>
<br>
<img src="media/my_profile_page.jpg" alt="admin page to manage a website">
<br>
<br>
<h2>Marketing strategies</h2>
<br>
- Social media Marketing:
<br>
<img src="media/facebook_page.jpg" alt="facebook page">
<br>
- using the Facebook page to create engagement, sharing daily posts, for a consistent online presence, <br>
with content like: new book releases, news about authors, creating polls and competitions, promoting the Book Club, a great feature for the website.<br>
<br>
- Email Marketing:
<br>
<img src="media/subscribe.jpg" alt="Subscribe page">
<br>
- with the Mailchimp subscribe form embedded in the website for users, several emails campagnes can be launched<br>
<br>
-  a monthly email with details about the book of the month <br>
<br>
- Special offers for subscribers: 15% off to certain categories from the website only for subscribers<br>
<br>
- Invitation to join the discussions in the book club for old customers<br>
<br>
<h3>Features left to implement</h3>
- Admin to approve comments and topics before they are published<br>
- Option to delete a comment for users<br>
<br>
<h2>Fixed Bugs</h2>
<br>
- NameError: name 'book_club' is not defined. Fix: urls path for book_club didn't include views. before book_club<br>
<br>
- WARNINGS:
?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace. Fix: remove the admin path from book_club urls.py <br>
<br>
- Subject.html page not working. Fix: The file subject.html had a space before the name which was causing the error<br>
<br>
<img src="media/subject.html_not_working.jpg" alt="creating a table of content for comments">
<br>
- Get_object_or404 not defined. Fix: get_object_or404 was not imported in bag/views.py<br>
<br>
<img src="media/get_object_or404_not_define.jpg" alt="error">
<br>
- TempleDoesNotExist. Fix: Folder name missing an s.<br>
<br>
<br>
<img src="media/folder_called_includes.jpg" alt="error">
<br>
<h3>Testing</h3><br>
<br>
<h2>Manual testing of each section of the site</h2>
- Admin:<br>
<br>
The admin can log through the admin pannel on https://thebookshelfchair-c10ecc9e636c.herokuapp.com/admin where they have access to the control pannel.<br>
<br>
The admin can add and delete books and categorise, approve users and create topics for the Book Club.<br>
<br>
<img src="media/AdminPannel.jpg" alt="admin pannel">
<br>
On the interface, the admin can edit books, delete them or add new ones.<br>
<br>
<img src="media/AdminEditDelete.jpg" alt="admin edit or delete books"><br>
<img src="media/AdminEdit.jpg" alt="admin edit books"><br>
<img src="media/AdminAdd.jpg" alt="admin add books"><br>
- User<br>
The User can create an account or login to an existing one.<br>
<img src="media/UserLogin.jpg" alt="new user login or register"><br>
<br>
When a new user is creating an account, he is promoted to add his email address and create a password.<br>
<img src="media/UserRegister.jpg" alt="user registration form"><br>
<br>
A confirmation email it is sent to the user. This section was tested with a temporary generated email, as per below.<br>
<br>
<img src="media/ConfirmationEmail.jpg" alt="confirmation email test"><br>
<img src="media/ConfEmailRec.jpg" alt="confirmation email test"><br>
<img src="media/ConfEmail1.jpg" alt="confirmation email test"><br>
<br> A verification email is sent to the new user, with a link which brings the user back to the bookstore's page.<br>
Once the email is confirmed, the user can start their shopping.<br>
Note that the user can add to bag without being login as well. But they can create an account or login to keep their order history<br>
<img src="media/UserCheckout.jpg" alt="unregistered user checkout"><br>
<img src="media/UserCheckout1.jpg" alt="unregistered user checkout"><br>
<br>
The user can browse the store, check out the categories and read descriptions of the books by opening them.<br>
The user can also update quantity when adding to bag a certain product<br>
<img src="media/UserAddToBag.jpg" alt="user adds to the shopping bag"><br>
<br>
A message pops up in the right corner every time a new product is added to the shopping bag.<br>
<img src="media/UserAddToBagMessage.jpg" alt="unregistered user checkout"><br>
The user can then edit their bag by clicking on the blue bag icon from the top right.<br>
There they can delete products or adjust quantity.<br>
<img src="media/UserEditBag.jpg" alt="user edit bag"><br>
<br>
The user can subscribe to the mailing list to keep in touch with offers and latest news about published books.<br>
A confirmation message about their subscription will be promted after they enter their email.<br>
<img src="media/SubscribeConf.jpg" alt="user subscribes"><br>
In case the email is already subscribed, the message to confirm that also shows up.<br>
<img src="media/Subscribe.jpg" alt="user already subscribed"><br>
<br>
The user can also navigate to the Book Club where he can join a topic already in debate.<br>
Their comment is automatically added to that specific topic.<br>
<img src="media/JoinTheChat.jpg" alt="user adds a comment to a topic in the Book Club"><br>
<img src="media/JoinTheChatAdded.jpg" alt="user's comment is added"><br>
<br>
A link to the book in discussion is added to transfer the user to the product, in case he would like to read more or purchase it.<br>
<br>
When the user checkout, a confirmation email is sent to his email address.<br>
<img src="media/CheckOutTest.jpg" alt="user's checkout bag"><br>
<img src="media/CheckOutTest1.jpg" alt="user's checkout bag"><br>


<h2>Data Model</h2>
<br>
The code has models, templates and views, working on the Django framework.<br>
There is a base.html to include the navigation bar and the footer, which is then extended in each other html files.<br>
Including a superuser to control the admin panel, the front end has an interactive interface for users to purchase products, leave comments and create topics.<br>
Automatic messages are poping to the side of the screen for each action regarding the shopping bag.<br>
The workspace was deployed to Heroku aat the end.<br>
<br>
<h3>Validator testing</h3>
<br>
-No errors were returned when passing through the PEP8 Linter - https://pep8ci.herokuapp.com/, only spaces and lines too long<br>
<br>
<img src="media/PIP3validator.jpg" alt="python validator">
<br>
- No errors were returned when passing through https://jigsaw.w3.org/css-validator/ <br>
<br>
<img src="media/CSSvalidator.jpg" alt="css validator">
<br>
<br><h2>Deployment</h2>
<br>
- This project had an initial deployment at the beginning to Heroku
<br>
A. Create a new Heroku app:
- Log to Heroku<br>
- On Dashboard, click on New and Create New App<br>
- Add a name to your new app and click create app<br>
<br>
B. Create a database on ElephantSQL.com<br>
- Create an account and create a new instance.<br>
-Select the free Tiny Turtle Plan and select a region.<br>
- Once the instance is created, copy the URL for the database<br>
<br>
C. Create Heroku Vars
<br>
- From Settings, Show Config Vars and add the data base URL, the secret key<br>
-Add the AWS keys, the database URL, stripe keys, email config <br>
<br>
D. Link the Heroku app to the repository<br>
- Go to Deploy Tab<br>
- Select Github for Deployment method<br>
- Search for your blog repo <br>
- Select Main as deployed branch and press deploy.<br>
- A new app link will be created. <br>
<br>
The depolyed project can be found here: https://thebookshelfchair-c10ecc9e636c.herokuapp.com/
<br>
<h2>Credits</h2>
<br>
- Stack Overflow<br>
- Bootique Ado walkthrough projects from Code Institute<br>
- <br>