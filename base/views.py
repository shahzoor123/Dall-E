from django.shortcuts import render

# Create your views here.
def home(request):
    import time
    date = time.gmtime()
    year = date.tm_year
    month = date.tm_mon
    day = date.tm_mday
    hour = date.tm_hour
    minute = date.tm_min
    second = date.tm_sec

    context = {
        'time' : time,
        'year' : year,
        'month' : month,
        'day' : day,
        'hour' : hour,
        'min' : minute,
        'second' : second,
    }
    
    return render(request, 'index.html', context)