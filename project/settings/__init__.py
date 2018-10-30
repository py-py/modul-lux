import os
from .base import *

environment = os.environ.get('ENVIRONMENT', 'dev')

if environment == 'prod':
    from .prod import *
if environment == 'dev':
    from .local import *

