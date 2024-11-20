from src.parser import parse_routes

def test_parse_routes():
    routes = parse_routes("examples/flask_app")
    print(routes)  # Debugging: Log the parsed routes
    assert len(routes) == 3  # Adjust this to match the actual count
