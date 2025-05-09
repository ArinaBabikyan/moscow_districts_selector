from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import SelectedDistrict

def map_view(request):
    return render(request, 'mapapp/map.html')

def save_district(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            district_name = data.get('district', None)

            if district_name:
                # Save the district name to the database or perform other actions here
                # Example: DistrictSelection.objects.create(name=district_name)
                selected_district, created = SelectedDistrict.objects.get_or_create(name=district_name)
                return JsonResponse({'message': 'District saved successfully'}, status=200)
            else:
                return JsonResponse({'error': 'District name is missing'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)


def get_selected_districts(request):
    # Get all selected districts from the database
    selected_districts = SelectedDistrict.objects.all().values_list('name', flat=True)
    return JsonResponse({'selectedDistricts': list(selected_districts)})

# views.py
from django.http import JsonResponse
from .models import SelectedDistrict
from django.views.decorators.csrf import csrf_exempt
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def toggle_district_selection(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            district_name = data['district']
            action = data['action']  # 'add' or 'remove'

            if action == 'add':
                # Add district to the selected list
                district, created = SelectedDistrict.objects.get_or_create(name=district_name)
                if created:
                    logger.info(f"Added district: {district_name}")
                else:
                    logger.info(f"District already selected: {district_name}")
            elif action == 'remove':
                # Remove district from the selected list
                affected_rows = SelectedDistrict.objects.filter(name=district_name).delete()
                if affected_rows[0] > 0:
                    logger.info(f"Removed district: {district_name}")
                else:
                    logger.warning(f"District not found for removal: {district_name}")

            return JsonResponse({'status': 'success'}, status=200)

        except Exception as e:
            logger.error(f"Error in toggling district selection: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)