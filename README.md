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
-No errors were returned when passing through the PEP8 Linter - https://pep8ci.herokuapp.com/
<br>
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
-Add the port value 800, the Cloudinary URL after creating a free account.<br>
<br>
D. Link the Heroku app to the repository<br>
- Go to Deploy Tab<br>
- Select Github for Deployment method<br>
- Search for your blog repo <br>
- Select Main as deployed branch and press deploy.<br>
- A new app link will be created. <br>
<br>
The depolyed project can be found here: https://the-office.herokuapp.com/
<br>
<h2>Credits</h2>
<br>
- Stack Overflow<br>
- Bootique Ado walkthrough projects from Code Institute<br>
- <br>