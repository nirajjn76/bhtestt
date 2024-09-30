import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Fetch the environment variable
    my_var = os.getenv('MY_ENV_VAR', 'Not set')

    # Create an HTML response
    html_content = f"""
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

    return func.HttpResponse(
        html_content,
        status_code=200,
        mimetype="text/html"
    )
