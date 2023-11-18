from django.shortcuts import render
from django.views import View
import psutil, time

class HomeView(View):
    '''View for home page'''
    
    def get(self, request):
        # Get cpu data
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_frequency = psutil.cpu_freq()
        
        # Format data collected from the system
        context = {
            'cpu_percent': cpu_percent,
            'cpu_count': cpu_count,
            'cpu_frequency': cpu_frequency,
        }
    
        return render(request, 'base.html', context=context)

