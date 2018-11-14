from .base import *

import os
from dotenv import load_dotenv

load_dotenv()
environment = os.getenv('ENVIRONMENT')

if environment == 'dev':
    from .local import *
if environment == 'prod':
    from .prod import *
if environment == 'pythonanywhere':
    from .prod_pythonanywhere import *
if not environment:
    raise Exception('Does not provide a setting file.')
