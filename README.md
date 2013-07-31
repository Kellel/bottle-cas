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



