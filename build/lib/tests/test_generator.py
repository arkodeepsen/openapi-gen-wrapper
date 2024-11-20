from src.generator import generate_spec

def test_generate_spec():
    routes = [
        {
            "route": "/hello",
            "methods": ["GET"],
            "description": "Returns a greeting message.",
            "parameters": []
        }
    ]
    spec = generate_spec(routes)
    assert "openapi: 3.0.0" in spec
    assert "/hello" in spec
    assert "Returns a greeting message." in spec
