from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'clubs', views.SportClubView)

urlpatterns = router.urls
