from django.http import HttpResponse
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from .scraper import scrape_service_pages

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

def scrape_data(request):
    scrape_service_pages()
    return HttpResponse('Scraping completed successfully!')
