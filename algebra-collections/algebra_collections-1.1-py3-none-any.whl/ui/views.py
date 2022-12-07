from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from algebra_calculator.views import *

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def duavariabel(request):
    template = loader.get_template('duavariabel.html')
    return HttpResponse(template.render())

@csrf_exempt
def tigavariabel(request):
    template = loader.get_template('tigavariabel.html')
    return HttpResponse(template.render())

@csrf_exempt
def calculateTwoExpression_LinearEquation(request):
      
  inp2Expression1 = str(request.POST['2expressions_1st'])
  inp2Expression2 = str(request.POST['2expressions_2nd'])

  variables = ['X', 'Y']

  equations = list()
  equations.append(inp2Expression1)
  equations.append(inp2Expression2)

  for i in range(len(equations)):
    equations[i] = equations[i].upper()

  result2E = str()
  r = list()

  try:
    r = LinearEquation.solve(len(equations), variables, equations)

    for i in range(len(variables)):
          temp = str(r[i])
          result2E += f"Value of {variables[i]} = {temp}\n"

    mydictionary = {
        "result2E" : result2E,
        "error" : False
    }
    return render(request, 'duavariabel.html', context=mydictionary)
  except:
    mydictionary = {
        "error" : True
    }
    return render(request, 'duavariabel.html', context=mydictionary)

@csrf_exempt
def calculateThreeExpression_LinearEquation(request):
  inp3Expression1 = request.POST['3expressions_1st']
  inp3Expression2 = request.POST['3expressions_2nd']
  inp3Expression3 = request.POST['3expressions_3rd']
  
  variables = ['X', 'Y', 'Z']

  equations = list()
  equations.append(inp3Expression1)
  equations.append(inp3Expression2)
  equations.append(inp3Expression3)

  for i in range(len(equations)):
        equations[i] = equations[i].upper()

  result3E = str()
  r = list()

  try:
    r = LinearEquation.solve(len(equations), variables, equations)
    for i in range(len(variables)):
          temp = str(r[i])
          result3E += f"Value of {variables[i]} = {temp}\n"

    mydictionary = {
      'result3E' : result3E,
      "error" : False
    }
          
    return render(request, 'tigavariabel.html', context=mydictionary)
  except:
    mydictionary = {
        "error" : True
    }
    return render(request, 'tigavariabel.html', context=mydictionary)