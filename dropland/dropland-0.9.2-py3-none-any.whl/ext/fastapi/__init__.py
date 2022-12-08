try:
    import starlette

    from .application import FastAPIApplication
    from .dependencies import query_locale, cookie_locale
    from .json import JsonResponse, JsonRequest
    from .permissions import HttpPermission, PermDepends, Authenticated, Admin

except ImportError:
    pass
