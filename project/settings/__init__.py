import os
from .base import *

environment = os.environ.get('ENVIRONMENT', 'dev')

if environment == 'dev':
    from .local import *
if environment == 'prod':
    from .prod import *
if environment == 'pythonanywhere':
    from .prod_pythonanywhere import *

