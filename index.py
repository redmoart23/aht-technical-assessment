from app import app
from utils.db import db


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
