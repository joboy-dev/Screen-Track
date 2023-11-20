from django.shortcuts import render
from django.views import View
import psutil
import pygetwindow as gw
import win32gui
import win32con
import win32api

from .utility_functions import get_open_apps, get_year
            

class HomeView(View):
    '''View for home page'''
    
    def get(self, request):
        # Get cpu data
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_frequency = psutil.cpu_freq()
        
        # open_apps = [window.title for window in gw.getAllWindows()]
        
        
        # Format data collected from the system
        context = {
            'cpu_percent': cpu_percent,
            'cpu_count': cpu_count,
            'cpu_frequency': cpu_frequency,
            'apps': get_open_apps()[2:],
            'user': self.request.user,
            'page_title': 'Home',
            'year': get_year()
        }
        
        return render(request, 'index.html', context)

