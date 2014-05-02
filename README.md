bottle-cas
==========

A CAS Client written with bottle.py

### Usage
```python

from bottle import route, run, request, bottle
from bottle_cas.client import CASClient
from bottle_cas.client import CASMiddleware
cas = CASClient()

app = bottle
app = CASMiddleware(app)

@route('/')
@cas.require
def index():
    user = request.environ['REMOTE_USER']
    return "Hello %s." % user

run(app=app)
```
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


