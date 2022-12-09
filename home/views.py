from django.shortcuts import render

# Create your views here.
def home(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/index.html', )
    else:
        return render(request, 'home/index.html', )

