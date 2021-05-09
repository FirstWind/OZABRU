from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.HumanView)
router.register(r'trainers', views.TrainersView)
router.register(r'cities', views.CityView)
router.register(r'locations', views.LocationView)
router.register(r'regions', views.RegionView)
router.register(r'kodevents', views.KodEventView)
router.register(r'participants', views.ParticipantView)
router.register(r'vidsporta', views.VidSportaView)
router.register(r'statusevent', views.StatusEventView)
router.register(r'referees', views.RefereeView)
router.register(r'commands', views.CommandView)
router.register(r'groups', views.GroupView)
router.register(r'userphone', views.UserPhoneView)

urlpatterns = router.urls
