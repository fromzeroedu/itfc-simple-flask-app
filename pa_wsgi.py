import os, sys
from dotenv import load_dotenv

python_anywhere_username = 'jorge3'
path = '/home/' + python_anywhere_username + '/opt/simple_flask_app'
if path not in sys.path:
    sys.path.append(path)

load_dotenv(os.path.join(path, '.flaskenv'))

from hello import app
app.debug = True

from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, evalex=True)
