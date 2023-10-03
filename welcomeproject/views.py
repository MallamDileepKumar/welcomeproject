from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    res = HttpResponse("""<html><body bg color = cyan><h1>Welcome to the Django projects</h1></body></html>""")
    return res
