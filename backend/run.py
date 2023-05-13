from main import create_app
from config import DevConfig
from exts import db

app = create_app(DevConfig)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()