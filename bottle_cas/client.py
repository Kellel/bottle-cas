#
# Bottle-CAS Client
# Written by: Kellen Fox
#
# This module aims to be a sane implementation of the CAS protocol written to be used with the bottle.py framework
#
"""
Bottle-CAS Client

CAS SSO Client for bottle applications
"""

from bottle import route, run, request, redirect, response
import urllib2
import urlparse
from functools import wraps
import time

#  Status codes returned by function validate().
TICKET_OK      = 0        #  Valid CAS server ticket found.
TICKET_NONE    = 1        #  No CAS server ticket found.
TICKET_INVALID = 2        #  Invalid CAS server ticket found.

class CASClient():
    def __init__(self):
        import config
        self._CAS_SERVER = config.CAS_SERVER
        self._CAS_LOGOUT_URL = config.CAS_LOGOUT_URL
        self._CAS_COOKIE = config.CAS_COOKIE
        self._MAX_COOKIE_AGE = config.MAX_COOKIE_AGE
        self._SECRET = config.SECRET
        self._DEBUG = config.DEBUG
        self._COOKIE_PATH = config.COOKIE_PATH

    def _do_login(self):
        url = request.urlparts
        newurl = (url[0],url[1],url[2],'',url[4])
        cas_url = self._CAS_SERVER + "/cas/login?service=" + urlparse.urlunsplit(newurl)
        redirect(cas_url)
    
    def require(self, fn):
        """
        Decorator to enable CAS authentication for a bottle route
    
        :Usage:
    
           @route('/foo')
           @require
           def foo():
          NOTE: The require statement must be used between the route definition and the function.
                If using an additional authentication scheme (LDAP) this should be defined below the CAS require
    
        :returns: A wrapped route that requres CAS authentication
        :rtype: `function`
        """
    
        @wraps(fn)
        def wrapper(*args, **kwargs):
            cookie = request.get_cookie(self._CAS_COOKIE, secret=self._SECRET)
            ticket = request.query.ticket;
            if cookie:
                if self._DEBUG:
                    print "Valid Cookie Found"
                request.environ['REMOTE_USER'] = cookie
                return fn(*args, **kwargs)
            if ticket:
                if self._DEBUG:
                    print "Ticket: %s recieved" % ticket
                status, user = self._validate(ticket)
                if status==TICKET_OK:
                    if self._DEBUG:
                        print "Ticket OK"
                    response.set_cookie(self._CAS_COOKIE, user, secret=self._SECRET, path=self._COOKIE_PATH, expires=time.time()+ 60*self._MAX_COOKIE_AGE)
                    request.environ["REMOTE_USER"] = user
                    # Remove the query variables from uri
                    url = request.urlparts
                    new_url = (url[0],url[1],url[2],'',url[4])
                    redirect(urlparse.urlunsplit(new_url))
                    #return fn(*args, **kwargs)
                else:
                    raise Exception("Ticket Validation FAILED!")
            self._do_login()
        return wrapper
    
    def logout(self):
        """
        Will Redirect a user to the CAS logout page
    
        :returns: Will not return
        :rtype: `None`
        """
        response.set_cookie(self._CAS_COOKIE, '', expires=0)
        redirect(urlparse.urljoin(self._CAS_SERVER, self._CAS_LOGOUT_URL))
    
    # A function to grab a xml tag. This isn't the best possible implementation but it works
    # It also doesn't require an external library
    def _parse_tag(self, str,tag):
        """
        Internal Function to parse a specific xml tag
    
        :Usage:
            _parse_tag(foo_string, "tag")
    
        :returns: the text contained within the tag specified
        :returns: `string`
        """
        tag1_pos1 = str.find("<" + tag)
        #  No tag found, return empty string.
        if tag1_pos1==-1: return ""
        tag1_pos2 = str.find(">",tag1_pos1)
        if tag1_pos2==-1: return ""
        tag2_pos1 = str.find("</" + tag,tag1_pos2)
        if tag2_pos1==-1: return ""
        return str[tag1_pos2+1:tag2_pos1].strip()
    
    # Validate the CAS ticket using CAS version 2
    def _validate(self, ticket):
        """
        Internal function to validate a CAS ticket
    
        :returns: ticket_status and username
        :rtype: `int` and `string`
        """
        url = request.urlparts
        newurl = (url[0],url[1],url[2],'',url[4])
        url_string = self._CAS_SERVER + "/cas/serviceValidate?ticket=" + ticket + "&service=" + urlparse.urlunsplit(newurl)
        validate_resp = urllib2.urlopen(url_string)
        resp = validate_resp.read()
        user = self._parse_tag(resp, "cas:user")
        ## For debug
        #print resp
        if user=='':
            return TICKET_INVALID, ""
        else:
            return TICKET_OK, user
    

if __name__ == '__main__':
    cas = CASClient()
    @route('/')
    @cas.require
    def index():
        user = request.environ.get('REMOTE_USER')
        resp =  """
            <a href="/thing">A page for authenticated clients</a>
            """
        return resp

    @route('/thing')
    @cas.require
    def thing():
        user = request.environ.get('REMOTE_USER')
        return "Hello, %s. This is a CAS client written in bottle" %user

    @route('/logout')
    def log_out():
        logout()
    run(host='localhost', port=8090)
