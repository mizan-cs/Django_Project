from django.shortcuts import render
from test_db.models import student

# Create your views here.

def main_page(request):

    return render(request,'test_sql.html')
