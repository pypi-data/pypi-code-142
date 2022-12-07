from django.urls import path
from . import views

urlpatterns = [
    path('TwoExpression_LinearEquations', views.duavariabel, name="duavariabel"),
    path('ThreeExpression_LinearEquations', views.tigavariabel, name="tigavariabel"),
    path('calculateTwoExpression_LinearEquation', views.calculateTwoExpression_LinearEquation, name="result1"),
    path('calculateThreeExpression_LinearEquation', views.calculateThreeExpression_LinearEquation, name="result2")
]