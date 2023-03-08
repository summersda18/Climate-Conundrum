from cProfile import label
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, redirect
from .forms import *
from .decorators import unauthenticated_user
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from .models import *

def home(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

@login_required(login_url='loginUser')
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

@login_required(login_url='loginUser')
def research_list(request):
    research = Research.objects.all()
    return render(request, 'research_list.html', {
        'research': research
    })
    
@login_required(login_url='loginUser')
def upload_research(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('research_list')
    else:
        form = ResearchForm()
    return render(request, 'upload_research.html', {
        'form': form
    })

def delete_research(request, pk):
    if request.method == 'POST':
        research = Research.objects.get(pk=pk)
        research.delete()
    return redirect('research_list')



def registerUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        messages.error(request, "Something went wrong!")
    form = NewUserForm()
    return render(request, 'registration.html', {'form':form})

@unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('home')

def buildGraph(values):
    location = getGraphData(values)
    climateFactors = []
    maxTempArr = []
    minTempArr = []
    avgTempArr = []
    windArr = []
    precipArr = []
    data = []
    dateOf = []

    for x in location:
        temp = ClimateFactor.objects.filter(date=x)
        dateOf.append(x.date)
        for y in temp:
            climateFactors.append(y)
    
    for climate in climateFactors:
        maxTempArr.append(climate.maxTemp)
        minTempArr.append(climate.minTemp)
        avgTempArr.append(climate.avgTemp)
        windArr.append(climate.avgWindSpeed)
        precipArr.append(climate.avgPrecipitation)
    
    fig = plt.figure()
    plt.plot(dateOf, maxTempArr, label ="Maximum Temperature")
    plt.plot(dateOf, minTempArr, label ="Minimum Temperature")
    plt.plot(dateOf, avgTempArr, label ="Average Temperature")

    fig2 = plt.figure()
    plt.plot(dateOf, windArr, label ="Average Wind Speed")

    fig3 = plt.figure()
    plt.plot(dateOf, precipArr, label ="Precipitation")

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    plt.close(fig)

    imgdata2 = StringIO()
    fig2.savefig(imgdata2, format='svg')
    imgdata2.seek(0)
    plt.close(fig2)

    imgdata3 = StringIO()
    fig3.savefig(imgdata3, format='svg')
    imgdata3.seek(0)
    plt.close(fig3)

    data.append(imgdata.getvalue())
    data.append(imgdata2.getvalue())
    data.append(imgdata3.getvalue())
    return data 

def getGraphData(values):
    if len(values) == 3:
        if int(values[1]) < int(values[2]):    
            str1 = values[1] + '-01-01'
            str2 = values[2] + '-12-31'
            location = DateAndLocation.objects.filter(city=values[0], date__range=[str1, str2])
        else:
            str1 = values[2] + '-01-01'
            str2 = values[1] + '-12-31'
            location = DateAndLocation.objects.filter(city=values[0], date__range=[str1, str2]) 
    else:
        location = DateAndLocation.objects.filter(city=values[0], date__year=values[1]).order_by('date')
    return location

def graph(request):
    postData = []
    currentData = ["Morrisville", "2021"]
    graph = buildGraph(currentData)
    if request.method == 'POST':
        form = GraphFrom(request.POST)
        if form.is_valid():
            for key in form.cleaned_data.keys():
                postData.append(form.cleaned_data[key])
            graph = buildGraph(postData)
    context = {
        'graph': graph[0],
        'graph2': graph[1],
        'graph3': graph[2]
    }
    return render(request, 'graphs.html', context)

def graphToYear(request):
    postData = []
    currentData = ["Morrisville", "2011", "2021"]
    graph = buildGraph(currentData)
    if request.method == 'POST':
        form = GraphByYearForm(request.POST)
        if form.is_valid():
            for key in form.cleaned_data.keys():
                postData.append(form.cleaned_data[key])
            graph = buildGraph(postData)
    context = {
        'graph': graph[0],
        'graph2': graph[1],
        'graph3': graph[2]
    }
    return render(request, 'graph_year_to_year.html', context)
