from django.shortcuts import render
from .models import Protein
# Create your views here.
def home(request):
    return render(request, 'home.html', {})    # request是必须的，返回home.html页面，{}参数传给html

def search_result(request):
    protein_name = request.POST['protein_name']
    not_found = ""
    try:
        protein_obj = Protein.objects.get(unp_id=protein_name)
        length = protein_obj.length
        domain_num = protein_obj.domain_num
        domain = protein_obj.domain
        return render(request, 'search_result.html', {"protein_name": protein_name, 
        "length": length, "domain_num": domain_num, "domain":domain, "not_found":not_found})
    except Protein.DoesNotExist:
        not_found = "Not found"
        return render(request, 'search_result.html', {"protein_name": protein_name, 
        "not_found":not_found})