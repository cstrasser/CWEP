from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def home(request):
   
    context_dict={'page_title':"Apes Web",
                  
                  'sidebar_list' : {
                  'Sales': "about.html", 'Service': "about.html" ,
                  'Accounting': "about.html", 'Production': "about.html", 'Purchasing': "about.html"},
                  'page_data': "- data from template variable is here -"}
  
    
    
    return render(request,'main.html', context_dict)

def about(request):
    context_dict = {'page_title': "APES Web About",'about_title': "About Apes Web", 'about_message' : "Version 0.0",
                    'dependency_list':["certifi (14.5.14)",
                                       "Django (1.8)" ,
                                       "django-pyodbc-azure (1.8.0.0)" ,
                                       "enum34 (1.0.4)",
                                       "pip (6.1.1)",
                                       "pyasn1 (0.1.7)",
                                       "pycparser (2.10)",
                                       "pyodbc (3.0.7)",
                                       "setuptools (12.0.5)",
                                       "six (1.9.0)",
                                       "sql-server.pyodbc (1.0)",
                                       "urllib3 (1.10.2)"]
                     }
    
    return render(request, 'about.html', context_dict)