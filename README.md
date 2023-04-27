# COP4521-Project
NOMNOM is a user-contributed database for fast food establishments. Its goal is to manage a database for displaying detailed information about restaurants and their menu to any visitor and allowing a registered user to contribute to that database by submitting ratings for both these elements.

The user interface is very intuitive, as navigation to all major features is available in the top navigation bar. It is worth reiterating that only a registered and signed in user may navigate to
the rating submission pages, so that is a feature that is not immediately apparent.

Imported python libraries include:
- os - ‘Miscellaneous operating system interfaces’ library
- sys - ‘System-specific parameters and functions’ library
- django - Django packages such as django.auth
- PIL - ‘Python Imaging Library’

Additional resources include:
- Django - Django is the chosen web framework for our website.
- Postgresql- PostgresSQL is the chosen database management system, in part because of its wide support by other resources we could use like Azure or AWS, and Djangos collection of specific features for postgres.
- AWS - Amazon Web Services was used to host our database so that it could be accessed remotely by connecting users.
- Django Crispy Forms - a Python package that uses built-in template packs to style Django forms.
- Bootstrap - Bootstrap is the chosen CSS framework for our website.

Group Contributions:
Lucca - Created initial django setup, added requirements.txt, template inheritance, bootstrap styling, about page, user registration, login/logout system, user profile page, staff only create restaurant, staff only create menu item, superuser only update/delete, pagination, menu view, sorting, filtering 
Brandon - Collected and formatted data from various restaurants for database and testing, collaborated on the website structure, collaborated on the user-created list functionality, restaurants page, prototyping, parallel processing implementation research, html design.

Rohith - Created Database Models, Created Rating System for restaurants and items, Set up database with PostgreSQL on AWS, Implemented list functionality.





Beyond the project, we implemented a user profile where users have a profile picture and can edit their credentials.




Parallel Processing component
If we were to solve an aspect of our project issue using parallel processing, a valuable place to use it would potentially be retrieving data from our database for displaying restaurants and their menu items in full on our website’s pages. On a much larger scale than what our website contains– being able to retrieve information about thousands of websites and their hundreds of food items, and every data field about those food items– methods to improve performance such as parallel processing are vital. It may also be relevant for our rating system, as if we store user ratings as individual records, we will need to improve performance to make that as efficient as simply and cheaply tracking the total number of ratings ever received and combining any new reviews with the current average. Improving performance through parallel processing will allow us to retain that valuable information, enabling greater control over the records and better management of our site.
Employing parallel processing in these contexts using the imported multiprocessing python library is simple. We can use a Pool class in order to dedicate a number of processors to any function we pass into the class’s methods. Since the page does not update itself automatically to display newly loaded restaurants, we would need to specify that we want the processes to wait for the full task to be complete, because we need to order the display, as on our website, we order restaurants on our home page by their user-given rating. To do this with our parallel processes, we would need to use the join() method.
