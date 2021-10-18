This app was made using django framework, the purpose is to create a REST API that could be used by an external frontend server.
And also be hosted in Heroku, that is the reason of the "Procfile" and "requirements" files. 
To make this possible I had to use utilitys displayed in the requirements.txt file, The most notable utility is "rest_framework"
For this test I was supposed to use the MySQL database provided by the company. Django requires to create some tables to operate for this reason 
I had to use a PostgreSQL database provided by Heroku because I did not have the privileges to create tables in the mentioned MySQL database.
To interact with the products there is an admin option to add products and categories (credentials must be provideds).
urls for the heroku site:
1. https://bsaletest-backend.herokuapp.com/ for the API
2. https://bsaletest-backend.herokuapp.com/admin for the admin site 
