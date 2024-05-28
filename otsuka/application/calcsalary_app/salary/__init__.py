from flask import Flask

app = Flask(__name__)
app.config.from_object('salary.config')

import salary.views