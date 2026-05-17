name : python flask sqlite3 login page 

description: Create a python flask based web application with sqlite3 as a database 

# create a login page 

## Instructions
    create the login page only , no registration page is needed 

1. **Architecture**
    - simple python3 flask based login page 
    - database is sqlite3 
    - login username = admin 
    - login password = admin

2. **Tech Stack**
    - python3 
    - flask 
    - sqlite3
    - HTML
    - css
    - js 
    - bootstrap (CDN)


3. **login button**
    - create a login button of blue in color 

4. **Database Design**
    - A users table holds the admin record with a hashed password (via werkzeug.security). On
  first run the app seeds admin/admin into the DB automatically. Flask sessions track
  logged-in state. This is how a real Flask app works, and the structure is easy to extend
   later.

5. **login page design**
    - A split panel view , with left part is blue and right part contains username and on the next line password field. At the bottom of this login button.

    - create a seperate templates directory that will hold the index.html page for the login .

6. **If login successfull**
    - If user able to make a successfull login with username admin and password admin , create a python flask flash message to display "Login Successfull"

7. **If login unsucessfull**
    - If user put wrong credentials then create a python flask flash message with error "Invalid creadentials"

8. **Create the requirements.txt**
    - As this is a python application create a requirements.txt , which contains the list of packages that are going to use for this project