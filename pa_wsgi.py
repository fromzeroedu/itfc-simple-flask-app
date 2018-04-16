import sys
python_anywhere_username = 'jorge3'
path = '/home/' + python_anywhere_username + '/opt/simple_flask_app'
if path not in sys.path:
    sys.path.append(path)

from hello import app as application

from hello import app
app.debug = True

from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, evalex=True)
