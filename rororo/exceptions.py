"""
=================
rororo.exceptions
=================

All exceptions from WebOb, routr and rororo in one place.

"""

from string import Template

from routr import exc as routr_exceptions
from schemify import ValidationError
from webob import exc as webob_exceptions


class HTTPServerError(webob_exceptions.HTTPServerError):
    """
    Modify server errors to print tracebacks in debug mode.
    """
    body_template_obj = Template("""${explanation}<br /><br />
<pre>${detail}</pre>
${html_comment}
""")


class ImproperlyConfigured(Exception):
    """
    Class for improperly configured errors.
    """


class NoRendererFound(ValueError):
    """
    Prettify message for "No renderer found" exception.
    """
    def __init__(self, renderer):
        message = 'Renderer {!r} does not exist.'.format(renderer)
        super(NoRendererFound, self).__init__(message)


def inject(module):
    """
    Inject all exceptions from module to global namespace.
    """
    for attr in dir(module):
        if attr.startswith('_') or attr in globals():
            continue

        value = getattr(module, attr)

        if isinstance(value, type) and issubclass(value, Exception):
            globals()[value.__name__] = value


inject(routr_exceptions)
inject(webob_exceptions)