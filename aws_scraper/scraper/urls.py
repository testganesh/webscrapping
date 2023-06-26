from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, scrape_data

# Create a router and register the ServiceViewSet
router = DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    
    # Scrape data
    path('scrape/', scrape_data, name='scrape_data'),
]
