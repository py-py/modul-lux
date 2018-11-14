from .base import *

from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.example')
environment = getenv('ENVIRONMENT')

if environment == 'dev':
    from .local import *
if environment == 'prod':
    from .prod import *
if environment == 'pythonanywhere':
    from .prod_pythonanywhere import *
if not environment:
    raise Exception('Does not provide a setting file.')

