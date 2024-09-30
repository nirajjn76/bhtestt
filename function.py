import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Fetch the environment variable
    my_var = os.getenv('MY_ENV_VAR', 'Not set')

    return func.HttpResponse(
        f"Value of MY_ENV_VAR: {my_var}",
        status_code=200
    )