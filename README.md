bottle-cas
==========

A CAS Client written with bottle.py

### Usage

```python

from bottle import route, run, request
from bottle-cas.client import require

@route('/')
@require
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



