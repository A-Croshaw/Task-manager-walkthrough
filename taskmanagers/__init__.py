import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["postgres://oxhgdmxx:Si6-gDcC_Y32rEKEcj_WsW_LkRrlAB8-@trumpet.db.elephantsql.com/oxhgdmxx"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["postgres://oxhgdmxx:Si6-gDcC_Y32rEKEcj_WsW_LkRrlAB8-@trumpet.db.elephantsql.com/oxhgdmxx"] = uri

db = SQLAlchemy(app)

from taskmanagers import routes  # noqa
