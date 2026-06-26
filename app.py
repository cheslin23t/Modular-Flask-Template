from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('flasksession', 'change-me')
app.config['APPLICATION_NAME'] = os.getenv('APPLICATION_NAME', 'Flask Template')


@app.context_processor
def inject_application_name():
    return {'application': {'name': app.config['APPLICATION_NAME']}}

from importlib import import_module
active_routes = ['index', 'account', 'dashboard']
for route in active_routes:
    m = import_module(f'modules.{route}.index')
    app.register_blueprint(m.app)

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)



@app.template_filter('humanize')
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = 0
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff // 30) + " months ago"
    return str(day_diff // 365) + " years ago"
app.run(host='0.0.0.0', port=8080)