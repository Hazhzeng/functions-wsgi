import azure.functions as func
from FlaskApp import app

main = func.WsgiMiddleware(app.wsgi_app).main
