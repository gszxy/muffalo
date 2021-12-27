import inspect
import types

from fastapi import exceptions


class MuffaloException(exceptions.HTTPException):
    status_code = 500
    message = "Unexpected Server Error"
    
    def __init__(self):
        attrs = inspect.getmembers(
            self,
            predicate=lambda i: not inspect.isroutine(i)
        )
        super(MuffaloException, self).__init__(
            self.status_code,
            {attr[0]: attr[1] for attr in attrs
             if not (attr[0].startswith('_') or attr[0] in ['status_code', 'args'])}
        )


class BadRequest(MuffaloException):
    status_code = 400
    message = "Invalid Input"
