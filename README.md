# The weather
A simple web app using Django and weather api (openweathermap) to preview the weather in some cities that user added. User could add or remove city.

* Demo link:http://mbweather.herokuapp.com/

# Setup Instruction
*	Create a new directory at a desired place in your file system
```
$ mkdir name_of_your_choice
$ cd name_of_your_choice
```
*	Create a virtual environment in recently created directory and activate it:
```

$ python -m venv wenv
$ ./wenv/Scripts/activate
```

*	Clone the repository and enter to the repository:
```
$ git clone https://github.com/mbairaq/the_weather.git
$ cd the_weather
```
*	Next, install the dependencies using pip:
```
pip install -r requirements.txt
```
*	Migrate your database.
```
$ python manage.py migrate
```

*	Once the migration is finished, you are ready to run the server.
```
 python manage.py runserver
```



* Visit [localhost:8000](http://127.0.0.1:8000/) in your browser to see how it looks.

