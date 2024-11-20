import os
import ast
import re

def parse_routes(project_path):
    """Parses Flask routes, HTTP methods, and potential parameters."""
    routes = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    tree = ast.parse(f.read(), filename=file_path)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):  # Look for route handlers
                            docstring = ast.get_docstring(node)
                        if isinstance(node, ast.Call):
                            if hasattr(node.func, 'attr') and node.func.attr == 'route':
                                route = node.args[0].value if node.args else None  # Changed .s to .value
                                methods = []
                                for keyword in node.keywords:
                                    if keyword.arg == 'methods':
                                        methods = [m.value for m in keyword.value.elts]  # Changed .s to .value
                                if route:
                                    path_variables = re.findall(r'<(\w+)>', route)
                                    routes.append({
                                        'route': route,
                                        'methods': methods,
                                        'description': docstring or "No description available",
                                        'parameters': [{'name': var, 'in': 'path', 'required': True, 'type': 'string'} for var in path_variables]
                                    })
    return routes
