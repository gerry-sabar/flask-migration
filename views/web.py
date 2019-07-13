from main import app
from models.log import Log

@app.route('/testing')
def index():
    log = Log.query.first();
    return 'First log is: ' + log.detail
