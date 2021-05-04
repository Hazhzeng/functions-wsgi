import azure.functions as func
from FastapiApp import app

main = func.AsgiMiddleware(app).main
