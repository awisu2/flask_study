flask_study
===========


commands
--------

- run virtual:
  - `souce venv/bin/activate`
- run: `docker-compose up`
- init-db: `docker-compose run app flask innit-db`
  - it's need after run db
- test: `docker-compose run app pip install -e . && pytest`
  - test on coverage: `docker-compose run app pip install -e . && coverage run -m pytest`


config
------

[FLASK\_ENV](http://flask.pocoo.org/docs/1.0/config/)

- *FLASK_ENV*: development (default: production)
