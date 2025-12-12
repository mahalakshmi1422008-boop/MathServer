# Ex.04 Design a Website for Server Side Processing
## Date:12/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:

```
math.html

<html>
<head>
    <title>Mileage Calculator</title>
    <style>
        body 
        {
            background: linear-gradient(gold);
        }
        .id1 
        {
            text-align: center;
            color: black;
        }
        .box 
        {
            text-align: center;
            width: 50%;
            background-color:cyan;
            border: solid 4px black;
            padding: 20px;
            margin: 50px auto;
        }
        .result 
        {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1 class="id1"><u>Calculate Mileage Here</u></h1>
    <div class="box">
        <h2><u>Mileage</u></h2>
        <h3>Mahalakshmi S(25018377)</h3>
    <form method="POST">
{% csrf_token %}
<div class="formelt">
Distance : <input type="text" name="distance" value="{{d}}"></input>(in km)<br/>
</div>
<div class="formelt">
Fuel consumed : <input type="text" name="fuel consumed" value="{{f}}"></input>(in L)<br/>
</div>
<div class="formelt">
<input type="submit" value="Calculate"></input><br/>
</div>
<div class="formelt">
Mileage : <input type="text" name="mileage" value="{{mileage}}"></input>km/L<br/>
</div>
</form>
</div>
</div>
</body>
</html>

views.py

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


urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mileage/',views.mileage,name="mileage"),
    path('',views.mileage,name="mileage")
]
```
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (68).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (67).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
