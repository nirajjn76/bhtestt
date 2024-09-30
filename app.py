from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def index():
    my_var = os.getenv('MY_ENV_VAR', 'Not set')
    return f"""
    <html>
        <head>
            <title>Environment Variable</title>
        </head>
        <body>
            <h1>Value of MY_ENV_VAR</h1>
            <p>{my_var}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
