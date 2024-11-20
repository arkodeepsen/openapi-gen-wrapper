import yaml

def generate_spec(routes):
    """Generates an OpenAPI spec with parameters."""
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "API Documentation",
            "version": "1.0.0"
        },
        "paths": {}
    }
    for route in routes:
        if route['route'] not in spec["paths"]:
            spec["paths"][route['route']] = {}
        for method in route['methods']:
            spec["paths"][route['route']][method.lower()] = {
                "parameters": route['parameters'],
                "responses": {
                    "200": {
                        "description": route['description']
                    }
                }
            }
    return yaml.dump(spec, sort_keys=False)
