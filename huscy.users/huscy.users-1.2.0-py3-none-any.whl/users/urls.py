import warnings

from rest_framework.routers import DefaultRouter

from huscy.users import views


warnings.warn(
    'This module is deprecated and might be removed in a future version. '
    'Please use `api_urls.py` instead.',
    DeprecationWarning
)


router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = router.urls
