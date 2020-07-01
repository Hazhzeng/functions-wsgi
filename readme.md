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

3. Use Azure Functions Core Tools to debug your project locally (e.g. http://localhost:7071/hello/Chris)
