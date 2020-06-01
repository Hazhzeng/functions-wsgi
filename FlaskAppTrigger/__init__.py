import logging

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi
from ..FlaskApp.wsgi import application

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(application).handle(req, context)
