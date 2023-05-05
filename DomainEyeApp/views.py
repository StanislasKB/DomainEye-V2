from django.shortcuts import render
from django.http import HttpResponse
import whois 
import json
from DomainEyeApp.models import History

def home_view(request):
    return  render(request, 'home_view.html')

    
def data_view(request):
    lien=''
    historique=History()
    
    if request.method=='POST':
        lien=request.POST['search']
        data=whois.whois(lien)           
        historique=History.objects.create(domain=lien)
        
    elif request.GET.get('search_history'):
        lien=str(request.GET.get('search_history'))
        data=whois.whois(lien)
        
       
        
    else :
        data={}
      
    
    
    return render(request, 'data_view.html',data)
    
    
def history_view(request):
    historique=History.objects.all()
    return render(request,'history_view.html',{'history':historique})