from rest_framework import routers
from mozio_providers.views import ProviderViewset, JeojsonViewset


router = routers.DefaultRouter()
router.register(r'providers', ProviderViewset)
router.register(r'jeojsons', JeojsonViewset)
