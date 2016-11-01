from flask import Flask
from services import s_s
from mps import m_s

app = Flask(__name__)
app.register_blueprint(s_s)
app.register_blueprint(m_s)
app.run(debug=True)

if __name__ == "__main__":
    app.run()