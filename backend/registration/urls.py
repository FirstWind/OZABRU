from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'reg_participant', views.RegParticipantView)

urlpatterns = router.urls