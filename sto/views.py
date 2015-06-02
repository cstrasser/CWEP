from django.shortcuts import render, redirect, get_object_or_404
from sto.models import STO , Customer, Contact, LocationMaster
from sto.forms import STOForm


def sto_list(request, status = 'Active'):
        sto_list = STO.objects.filter(status = status, stid__lte=20239).select_related('customer_location__customer') #stid__lte 20239 to fix database error 
        count = sto_list.count()
        context ={'list': sto_list, 'count': count}
        return render(request, 'sto/listview.html', context)


def sto_form(request, stid ):
        sto = get_object_or_404(STO, pk=stid)
        
        try:
            contact = sto.contact
        except:   
            contact = 'none'
                            
        if request.method == 'POST':
                form = STOForm(request.POST, instance =sto)
                if form.is_valid():
                     form = form.save()
                     form.save()
                     return render(request,'sto/stoform.html', {'form':form, 'stid': stid})
                else:
                     print form.errors.as_data()
                     return redirect('/sto')
        else:
                
                form = STOForm(instance=sto)
                
        context = {'form':form, 'stid': stid, 'customer_name':sto.customer_location.customer,
                   'contact':contact}        
        return render(request,'sto/stoform.html', context)
