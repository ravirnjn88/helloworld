from flask import Flask
from services import s_s
from mps import m_s

application = Flask(__name__)
application.register_blueprint(s_s)
application.register_blueprint(m_s)


if __name__ == "__main__":
    application.run()
