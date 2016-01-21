A demonstration of a Personal API.

# Local Setup

I assume you are running postreSQL locally

* Clone this repo
* `virtualenv venv` # initialize a virtual environment [only once]
* `. ./activate.sh` # to activate the virtual environment
* `pip install -r requirements.txt` # install the dependencies
* rename `.env_sample` to `.env` and update the credentials
* make manage.py executable
* `./manage.py db upgrade` # create the database
* `./manage.py runserver` # execute the program

To cleanup your local directory run `./cleanup.sh`

# Documentation

The documentation is located on [Apiary](http://docs.apithyself.apiary.io).

# Testing

* `./manage.py test` # run the tests in the [tests folder](https://github.com/thinkingserious/apithyself/blob/master/test)

If you are running the tests for the very first time with empty DBs, they will fail upon first execution, but then subsequently pass
