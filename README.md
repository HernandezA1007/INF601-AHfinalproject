 - INF601 - Advanced Programming in Python
 - Antonio Hernandez
 - Final Project

# INF601 Final Project


### This final project focuses on using the Flask framework to create a watch list similar to my mini
project 3 application; the to do list. The application allows the user to create and manage a movie list.
By utilizing the Utelly API to search for movies and shows and adding them to their list. The user registers
and has their own individual account to save their data. The purpose of the project is so the user has all their
movies and shows in one place rather than multiple different streaming platforms and such apps.

---

Following ideas for list:  
- search, add, and share with others your movie and show list
- could also work for books, need to find an API
- ...

## Quick Start

> Before starting, look at requirements.txt to install the necessary packages

`pip install -r requirements.txt`

> This project requires you to initialize the database yourself
`flask --app movie_list init-db`'`
> After initializing, you run the application
`flask --app movie_list --debug run`
> Your application will redirect to your browser or check your console and click: http://127.0.0.1:5000/

### Older version followed my mini project 03 using Flask to make a to-do list
This one somewhat follows how mine would turn out, need to build in the Utelly API, login is broken

To start up the project, you can:
  - Download/Clone the project
  - RapidAPI/Utelly to help with the API process <https://rapidapi.com/blog/utelly-api-with-java-python-php-ruby-javascript-examples/>
  - Though, in a different language, step-by-step help <https://tutorial.helloflask.com/>

Example of how some code looks below: 
```python
import os
import flask from Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Watchlist'

...


```

## New start up installation:
First:
`clone, copy, or start your own project`
`create and activate your virtual environment`
`pip install -r requirements.txt`
Now in the console, to generate data
`flask forge`
After complete, you may run by typing in console:
`flask run`
Example template of the watchlist is given:
> Either you're redirected to your browser or click the http://127.0.0.1:5000/

