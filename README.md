# To-DO List
App To-Do List create with Django.

[![Build Status](https://travis-ci.org/carlos-moreno/to-do-list.svg?branch=master)](https://travis-ci.org/carlos-moreno/to-do-list)

## How to run?

1 - Clone the repository.
``` console
git clone https://github.com/carlos-moreno/to-do-list.git
```
2 - Go to the project directory.
``` console
cd to-do-list
```
3 - Create a virtualenv with Python 3.6+.
``` console
python -m venv .to-do-list
```
4 - Activate virtualenv.
``` console
source .to-do-list/bin/activate
```
5 - Install the dependencies.
``` console
pip install -r requirements.txt
```
6 - Configure the instance with .env.
``` console
cp contrib/env-sample .env
```
7 - Run the tests.
``` console
python manage.py test
```
8 - Run makemigrations and migrate.
``` console
python manage.py makemigrations
python manage.py migrate
```
9 - Run the application
``` console
python manage.py runserver
```
