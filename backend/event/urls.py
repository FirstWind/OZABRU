from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'programevent', views.ProgramEventView)
router.register(r'events', views.EventView)
router.register(r'disciplineprogram', views.DisciplineProgramView)
router.register(r'crossgroup', views.CrossGroupView)
router.register(r'relayrace', views.RelayRaceView)

urlpatterns = router.urls