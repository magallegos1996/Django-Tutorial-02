# Django Tutorial 02
### Based on: [Corey Schafer's Django Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer)
 
 ### How to run the the project
 
 First, clone this repository with the following command:
 ```sh
$ git clone https://github.com/magallegos1996/Django-Tutorial-02.git
```
Once you've cloned this repo, please change to the root directory:
 ```sh
$ cd Django-Tutorial-02
```
Then, execute the following command to create a python virtual environment
 ```sh
$ py -m venv env
```
This will create a directory called  ```env```. Enter to this directory using the following command
 ```sh
$ cd env
```
Next, execute the  ```activate.bat``` that is inside the ```Scripts``` directory. Please, follow this steps.
 ```sh
$ cd Scripts
$ activate.bat
```
Now, you have to return to ```Django-Tutorial-02``` folder so you can install all the requirements needed to run this project. In order to do so, from the ```Django-Tutorial-02``` directory, execute this.
 ```sh
$ pip install -r requirements.txt
```
Also, you need to manually install Crispy Forms and Pillow.
 ```sh
$ pip install django-crispy-forms
$ pip install Pillow
```
At this point, you will be able to run the project. But first, you have to do some additional steps. 

Place yourself into ```django_project``` directory
 ```sh
$ cd django_project
```
Run the following command to make migrations
 ```sh
$ py manage.py makemigrations
```
Then, run those migrations throught this command
```sh
$ py manage.py migrate
```
And finally, run the server with the follwing command
 ```sh
py manage.py runserver
```
Open your browser and go to: http://localhost:8000/

If you don't want to create a new user to get full access to the the demo, you can use this credentials:

* **Username:** marcelo
* **Password:** Ioet.1000
