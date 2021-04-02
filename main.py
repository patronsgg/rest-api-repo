from flask import Flask
from data import db_session
import jobs_api

app = Flask(__name__)


def main():
    db_session.global_init('db/mars_db.sqlite')
    app.register_blueprint(jobs_api.blueprint)
    app.run()


main()