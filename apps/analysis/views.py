from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

from .forms import UploadAntique
from .models import Antique
from .analyze import analyze_image

def analysis(request):
    form = UploadAntique()
    context = {'form': 'form'}
    return render(request, 'analysis.html', context)

def analyse_image_api(request):
    if request.method == 'POST':
        
        # create a form instance, passing in the POST data from javascript fetch
        form = UploadAntique(request.POST, request.FILES)
        if form.is_valid():
            antique = form.save(commit=False) # Don't save to DB yet
            if request.user.is_authenticated:
                antique.user = request.user
            antique.save() # Now save to DB after setting user
            
            # Call gemini API here with the uploaded image and get the analysis results
            analysis_results = analyze_image(antique.image.path)

            if analysis_results:
                # Update the Antique instance with analysis results
                antique.title = analysis_results.get('title', 'Unknown Title')
                antique.year = analysis_results.get('year', 0)
                antique.description = analysis_results.get('description', '')

                # Save the updated Antique instance
                antique.save()

            return JsonResponse({'success': True, 'result': analysis_results})
        else:
            # If the form is not valid, return a JSON error response
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

