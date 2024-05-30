import json
from functools import wraps

import flask


def api_response(json_content=True):
    """
    decorator that wraps function return value in response dictionary:

    ```python
    {
        'data': <return value>,
        'error': None
    }
    ```
    """

    def decorator(function):
        @wraps(function)
        def get_api_response():
            result = function()

            if isinstance(result, flask.Response) and json_content:
                result.set_data(json.dumps({
                    'data': result.get_data(as_text=True),
                    'error': None,
                }))
                result.headers.set('Content-Type', 'application/json')

                return result
            elif isinstance(result, flask.Response):
                return result

            return {
                'data': result,
                'error': None
            }

        return get_api_response

    return decorator
