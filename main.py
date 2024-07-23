from flask.cli import FlaskGroup
from src import create_app

# Create Flask application instance
app = create_app()

# Create CLI group instance
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
