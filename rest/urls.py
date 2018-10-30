from rest_framework import routers
from rest.views import *

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
