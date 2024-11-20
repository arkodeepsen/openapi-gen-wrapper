import click
from .parser import parse_routes
from .generator import generate_spec

@click.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--output', default='openapi_spec.yaml', help='Output file for OpenAPI spec.')
def main(project_path, output):
    """Generates an OpenAPI spec from a Python project."""
    routes = parse_routes(project_path)
    spec = generate_spec(routes)
    with open(output, 'w') as f:
        f.write(spec)
    click.echo(f"OpenAPI spec generated: {output}")

if __name__ == "__main__":
    main()
