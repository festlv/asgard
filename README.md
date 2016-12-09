Simple __CRM__ for a hackerspace/makerspace
-----------------------------------------------

Warning: very much work in progress.

Requires: python2

Installation:

    git clone git@github.com:festlv/asgard.git asgard
    cd asgard/
    virtualenv-2.7 .env
    source .env/bin/activate
    pip install -r requirements.txt
    cp asgard/local_settings.py.example asgard/local_settings.py
    vim asgard/local_settings.py # change database
    ./manage.py migrate
    ./manage.py runserver

