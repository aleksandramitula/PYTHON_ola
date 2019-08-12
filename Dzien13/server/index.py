from flask import render_template
from Dzien13.server.app import app_connexion
#from Dzien13.server.models import Album, AlbumSchema

# Get the application instance
connex_app = app_connexion

# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:8080/
    :return:        the rendered template
    """
    return "<h1>That is REST API example</h1>"


if __name__ == "__main__":
    connex_app.run(port=8080, debug=True)