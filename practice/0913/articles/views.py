from django.shortcuts import render
# render와 
# Create your views here.
def index(request):
  # 로직이 들어가야함
  return render(request, 'articles/index.html')