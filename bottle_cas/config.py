# Url of sso cas server
CAS_SERVER = "https://websso.example.com"

# This is probably fine
CAS_LOGOUT_URL = "/cas/logout"

# The name of your cookie
CAS_COOKIE = "CAS"

# The top level that the cookie should be stored
COOKIE_PATH = '/'

# Duration of cookie before revalidating to cas server
TIMEOUT = 600

# Your cookie encryption key
SECRET = "SUPER_SECRET_PASSPHRASE"

# Store sessions in non https connections
# WARNING: this makes session hijacking silly easy. PLS set this to False for production use
ALLOW_HTTP = True

# Turn on debug messages in logfiles
DEBUG = 1

# Configure Beaker session type
# http://beaker.readthedocs.io/en/latest/configuration.html
# File is default to allow multiple instances of beaker to share cached data
BEAKER_TYPE = 'file'

# Specifies Beaker data location
BEAKER_DATA_DIR = '/tmp/beaker/data'

# Specifies Beaker lock location
BEAKER_LOCK_DIR = '/tmp/beaker/lock'
