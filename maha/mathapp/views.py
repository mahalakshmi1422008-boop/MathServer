from django.shortcuts import render
def mileage(request):
    context={}
    context['mileage'] = "0"
    context['d'] = "0"
    context['f'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        d= request.POST.get('distance','0')
        f = request.POST.get('fuel consumed','0')
        print('request=',request)
        print('distance=',d)
        print('fuel consumed=',f)
        mileage = int(d)/int(f)
        context['mileage'] = mileage
        context['d'] = d
        context['f'] = f
        print('Mileage=',mileage)
    return render(request,'mathapp/math.html',context)