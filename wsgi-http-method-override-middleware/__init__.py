from webob import Request


class HttpMethodOverrideMiddleware(object):
    """WSGI middleware for overriding HTTP Request Method for RESTful support.

    Overriding is authorized only for the HTTP POST method.
    HTML forms can override by providing an additional input.
    Javascript calls can override by providing a specific header.
    """
    def __init__(self, application,
        input_name='REQUEST_METHOD_OVERRIDE',
        header_name='X-HTTP-Method-Override',
        authorized_methods=('PUT', 'DELETE', 'OPTIONS', 'PATCH')):
        """
        :application: The WSGI application.
        :input_name:  The overriding form input name.
            Default value: 'REQUEST_METHOD_OVERRIDE'.
        :header_name: The overriding HTTP header for javascript calls.
            Default value: 'X-HTTP-Method-Override'.
        :authorized_methods: The set of authorized HTTP methods.
            Default value: ('PUT', 'DELETE', 'OPTIONS', 'PATCH').
        """
        if not callable(application):
            raise TypeError('Application must be callable, but {0!r} is not '
                            'callable'.format(application))
        self.application = application
        self.input_name = input_name
        self.header_name = header_name
        self.authorized_methods = authorized_methods

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'POST':
            request = Request(environ)

            if self.input_name in request.POST:
                request_method = request.POST.get(self.input_name).upper()
            elif self.header_name in request.headers:
                request_method = request.headers.get(self.header_name).upper()
            else:
                request_method = None

            if request_method in self.authorized_methods:
                environ['REQUEST_METHOD'] = request_method

        return self.application(environ, start_response)
