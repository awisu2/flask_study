flask_study
===========

### virtualenvの利用について

開発環境はdockerで構成しています。そのため、virtualenvの利用は想定していません。  
ですが、deployシステムに採用しているzappaはvirtualenvの利用が必要なため、deloy時にだけvenvを作成及びinstallを行うようにしています。

commands
--------

- run virtual:
  - `souce venv/bin/activate`
- run: `docker-compose up`
- init-db: `docker-compose run app flask innit-db`
  - it's need after run db
- test: `docker-compose run app pip install -e . && pytest`
  - test on coverage: `docker-compose run app pip install -e . && coverage run -m pytest`

deploy & update
---------------

`sh bin/deploy.sh`

if you want first time deploy or undeploy. `sh bin/deploy.sh deploy` or `sh bin/deploy.sh undeploy`

config
------

[FLASK\_ENV](http://flask.pocoo.org/docs/1.0/config/)

- *FLASK_ENV*: development (default: production)
