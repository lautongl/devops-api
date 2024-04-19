from application import create_app
import os


if os.getenv('FLASK_ENV') == "development":
    app = create_app('config.DevConfig')
else:
    app = create_app('config.ProdConfig')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")