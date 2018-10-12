import os
from .base import *

environment = os.environ.get('ENVIRONMENT', 'dev')

if environment == 'prod':
    from .local import *
if environment == 'dev':
    from .prod import *

