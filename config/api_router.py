from django.conf import settings
from alacl_cutter.webwares.views import ProductViewSet, SetViewSet, CategoryViewSet,TechnologyViewSet

from rest_framework.routers import DefaultRouter, SimpleRouter

from alacl_cutter.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sets", SetViewSet)
router.register("products", ProductViewSet)
router.register("categorys", CategoryViewSet)
router.register("technologys", TechnologyViewSet)

app_name = "api"
urlpatterns = router.urls