def api_response():
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
        def get_api_response():
            return {
                'data': function(),
                'error': None
            }
        return get_api_response

    return decorator
