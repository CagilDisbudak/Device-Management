from celery import shared_task
from CaseProject.models import LocationHistory

@shared_task
def process_location_data(locations):
    LocationHistory.objects.bulk_create(locations)