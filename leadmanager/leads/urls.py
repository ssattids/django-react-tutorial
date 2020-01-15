from rest_framework import routers
#from api file import the view set
from .api import LeadViewSet

#register the routes
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

#give us all the CRUD urls
urlpatterns = router.urls