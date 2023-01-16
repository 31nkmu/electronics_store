# Electronics store (backend)
___
* First clone from repository to your local folder using command

    * ` git clone git@github.com:31nkmu/electronics_store.git `
* change dir using command
  * `cd electronics_store`
* Create virtual environment using command
    * ` python3 -m venv <name of your environment> `

* Activate your virtual environment
    * ` source <name of your environment>/bin/activate `

* install requirements.py with command
    * ` pip install -r requirements.txt `

* create file .env
    * ` touch .env `

* write your data in .env (see evn_example)

* migrate with command
    * `./manage.py migrate`
* finally you can run your project
    * ` ./manage.py runserver `
    or 
    ` python3 manage.py runserver ` 
    or 
    ` make run `
---

* you can use Makefile
  * create superuser
      * ` make user` is `./manage.py createsuperuser`
  * migrate
      * `make migrate` is `./manage.py makemigrations` && `./manage.py migrate`
  * run celery
      * `make celery` is `celery -A config worker -l debug`
  * run beat
    * `make beat` is `celery -A config beat`
  * run ngrok to provide the api to frontend
    * `make ngrok` is `ngrok http 8000`