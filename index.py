from app import app
from utils.db import db
from dotenv import load_dotenv
import logging
import os

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV') == 'dev'
PORT = int(os.getenv('PORT', 5000))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    if not FLASK_ENV:
        from waitress import serve
        logging.info(f"Starting Waitress server on port {PORT}...")
        serve(app, host="0.0.0.0", port=PORT)
    else:
        app.run(host='0.0.0.0', port=PORT, debug=True)
