# Bandersnatch

![Bandersnatch Picture](images/netflix.jpg)  

### What is this? 
A re-make of netflix's bandersnatch game as a web app created with Django. This is essentially a choose your own adventure book. All of the paths are based around netflix show black mirrow episode "Bandersnatch". This currently comes pre-loaded with one story that I created. a future feature set will be to give users the ability to create their own stories. 


### Getting Started
- Make sure you have [python3](https://www.python.org/download/releases/3.0/) installed on your machine and [pip](https://pip.pypa.io/en/stable/installing/)
- From the root directory run `source env/bin/activate`
- Get into the retro folder `cd retro` and then `python3 manage.py runserver`
- Navigate to `http://localhost:8000/` to create a user and play Bandersnatch
- You then should see this after you create your user !
<img src="images/screenshot.png" width="100" height="100">

### Possible Paths

<img src="images/paths.jpg" width="100" height="200">

These are the inspiration to all the possible [paths](https://www.polygon.com/2018/12/29/18159525/black-mirror-bandersnatch-all-endings-guide-netflix) in the game

### Database Model
![Model](images/model.png)
This is the basic model for the database

### Personalizing 
- Feel free to fork this project and create your own stories! The database model is 

### Planned Features
- Create a story dashboard for admin
- Host on Heroku

## To Do 
- Get Next stage to work

<!--
### Usefull Development Commands 
- `source env/bin/activate`
- `python3 manage.py runserver`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

### Admin User 
- User: `andybui`
- Password: `Fivestar54`
-->

 
