from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask('website')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/brady/website/website/blog.db'
db = SQLAlchemy(app)

import website.views
import website.models

if __name__ == '__main__':
    app.run()