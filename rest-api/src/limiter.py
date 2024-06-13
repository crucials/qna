import os

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


limiter = Limiter(  
    get_remote_address,
    # default_limits=['200 per day', '10 per second'],
    storage_uri=os.environ.get('REDIS_URL') or 'memory://',
)
