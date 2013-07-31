bottle-cas
==========

A CAS Client written with bottle.py

### Usage
```python

from bottle import route, run, request
from bottle_cas import client
cas = client()

@route('/')
@cas.require
def index():
    user = request.environ['REMOTE_USER']
    return "Hello %s." % user

run()
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


