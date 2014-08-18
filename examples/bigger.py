from bottle import route, request
import bottle
from bottle_cas import CASClient, CASMiddleware

# My other project http://github.com/Kellel/ProxyMiddleware
from ProxyMiddleware.ProxyMiddleware import ReverseProxied

cas = CASClient()
application = ReverseProxied(CASMiddleware(bottle.default_app()))

@route('/')
def index():
    resp =  """
        <a href="/thing">A page for authenticated clients</a>
        """
    return resp

@route('/test')
@cas.test_login
def test():
    username = None
    status = request.environ.get('REMOTE_USER_STATUS')

    if status == 'VALID':
        username = request.envrion.get('REMOTE_USER')

    return "User {}, is a {} user!".format(username, status)

@route('/thing')
@cas.require
def thing():
    user = request.environ.get('REMOTE_USER')
    return "Hello, %s. This is a CAS client written in bottle\n <a href='logout'>Logout</a>" %user

@route('/logout')
def log_out():
    cas.logout('http://reddit.com/')

run(app=application,host='localhost', port=8001)
