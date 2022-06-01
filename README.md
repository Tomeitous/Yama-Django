# Yama-Django
## Django project for small clubs or groups

![Main view](https://i.imgur.com/YAYdqRR.png)

### You can add people and series to the database. Add comments under the series. Register and login, which is required to edit and add anything to the database. 



## How to test

install virutalenv
>  $ sudo apt-get -y install virtualenv

Create a new virtualenv
> $ virtualenv --system-site-packages -p python3 env/

use virtual enviroment
> $ source env/bin/activate

add django to requirements
> $ cat requirements.txt
django

install requirements
> $ pip install -r requirements.txt

go to yama folder
> $ cd yama_copy

![Tree](https://i.imgur.com/83p4g2x.png)

run the testserver
> $ ./manage.py runserver

open 127.0.0.1:8000/yamanians on your browse

