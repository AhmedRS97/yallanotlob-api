# yallanotlob-api
An API for yallanotlob, this API is very basic and doesn't have any Authentication. we can make the API connect to any frontend framework. we will use react for an example, but you're free to choose whatever frontend framework you want.

# System Requirements:
1. any linux OS (prefered OS are [fedora](https://getfedora.org/) or [ubuntu](https://www.ubuntu.com/download)).
2. pyhon 3 is installed, it's installed by default on popular OS like fedora and ubuntu. but if you dont have it, here's a guide to install it on Ubunut https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04 
3. virtualenv is installed, here's a guide to install it https://linuxhint.com/python-virtualenv-tutorial/
4. npm is installed, here's a guide https://www.tecmint.com/install-nodejs-npm-in-centos-ubuntu/

# Installation Guide:
- First, Create Virtual environment for the project, in terminal type the following:
```
mkdir ~/yallanotlob-project/ && cd ~/yallanotlob-project/
virtualenv yallanotlob-env
```
- then we will clone and download the project from github:
```
git clone https://github.com/D0nQuixote/yallanotlob-api.git
```
- now we have to activate the environment:
```
source yallanotlob-env/bin/activate
```
- then we will install the project package requirements from requirements.txt, like this:
```
cd yallanotlob/
pip3 install -r requirements.txt
```
> this will install django and django REST API and few other packages.
- now we need to migrate the models to the database (we are using sqlite3) :
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- now we can run the django server by this command:
```
python3 manage.py runserver
```
now you can open http://localhost:8000/ or see the ui of the API by opening http://localhost:8000/api/meal-list/ but you'll find it empty. you can interact with the ui and create new Meal and send a POST request to the API to store the Meal content to the database. and if you don't want to add content via the API, then you can make a Super User to add content via the Admin panel.
> if you want to create a super user that can open the admin panel (eg. http://localhost:8000/admin/) and add content to the models,
- we can create the super user by this command:
```
python3 manage.py createsuperuser
```
> you'll be asked for a username, password, password confirmation, and email information. after you crate the super user, open http://localhost:8000/admin/ and login, then you'll see the Meal and Order models.

# the API urls and resources:
Anonymous and authenticated users have full access on the API and can get a list of Meals, add/remove Meals to the meals list, get the details of a meal, get a list of Orders, add/remove Orders to the orders list and get the details of an Order.
here's the urls:
- http://localhost:8000/api/meal-list/
- http://localhost:8000/api/meal/(<pk>)/   # the (<pk>) at the end is the id number of the meal
- http://localhost:8000/api/order-list/
- http://localhost:8000/api/order/(<pk>)/  # the (<pk>) at the end is the id number of the order
