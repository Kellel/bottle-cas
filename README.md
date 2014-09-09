bottle-cas
==========

[![Build Status](https://travis-ci.org/Kellel/bottle-cas.svg?branch=master)](https://travis-ci.org/Kellel/bottle-cas)

A CAS Client written with bottle.py

### Usage
```python

from bottle import route, run, request, Bottle
from bottle_cas.client import CASClient
from bottle_cas.client import CASMiddleware
cas = CASClient()

app = Bottle()
app = CASMiddleware(app)

@route('/')
@cas.require
def index():
    user = request.environ['REMOTE_USER']
    return "Hello %s." % user

run(app=app)
```
A more complete example can be found within the client (bottle_cas/client.py). Try running it!

### Installation
```bash
python setup.py build
python setup.py install
```
### Configuration
Configuration should be done in the config.py file located in your python site-packages
```bash
cd /usr/lib/python2.7/site-packages/bottle_cas
vim config.py
```

You really should only need to edit `CAS_SERVER` to get this working.
```bash
CAS_SERVER = "https://sso.domian.com" # sso server you would like to auth against
CAS_LOGOUT_URL = "/cas/logout" # The url of the logout
CAS_COOKIE = "CAS" # Name of the cookie
COOKIE_PATH = '/'
MAX_COOKIE_AGE = 1
SECRET = "PLOX_MAKE_DIS_SECRET"
DEBUG = 1
```



