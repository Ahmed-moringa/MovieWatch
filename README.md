# Spotlight

>[Ahmed Mohamed](https://github.com/Ahmed-moringa)  
  
# Description  
An application that allows an admin to create movies with date,price and seats available and a user to purchase a ticket for a certain movie and number of seats.

## Screenshots 
###### Home page

[![moviewatch.png](https://i.postimg.cc/7hkRYJsb/moviewatch.png)](https://postimg.cc/YGdRd0ww)

## User Story  
  
* View available movies and their details
* Add a movie with date and price
* Purchase tickets of listed movies
* Search for movies
* Download tickets
* View booking history
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Ahmed-moringa/MovieWatch.git 
```
##### Navigate into the folder 
 ```bash 
cd MovieWatch
```
##### Install and activate Virtual Environment
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make Migrations  
 ```bash 
python manage.py makemigrations spotlight
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python](https://www.python.org/)  
* [Django](https://docs.djangoproject.com/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* Problem with setting dates 
  
## Contact Information   
If you have any question or contributions, please email me at [ahmed.mohamed@student.moringaschool.com]  
  
## License 

* Copyright (c) 2022 **Ahmed Mohamed**