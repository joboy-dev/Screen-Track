from django.shortcuts import render
from django.views import View

class HomeView(View):
    '''View for home page'''
    
    def get(self):
        return render(self.request, 'base.html')
