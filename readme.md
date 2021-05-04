1. Change host.json to remove the http prefix
```json
"extensions": {
  "http": {
    "routePrefix": ""
  }
}
```

2. Change FlaskAppTrigger/function.json to enable HTTP verbs
```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get",
        "post",
        "put",
        "delete"
      ],
      "route": "/{*route}"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

3. Migrate your flask app into FlaskApp/ folder.
4. Change module import statements, FlaskApp/app.py for guidance.
```python
import azure.functions as func
from FastapiApp import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
```
or
```python
import azure.functions as func
from FlaskApp import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

```
