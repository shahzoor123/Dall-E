from django.shortcuts import render
import openai
import time

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


def get_api(request):

    context = {}

    if request.method == "POST":
        prompt_text = request.POST['prompt_key']

        openai.api_key = "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"
        response = openai.Image.create(
        prompt= f"{prompt_text}",
        n=6,
        size="1024x1024"

        )
        
        image_url = response['data'][0]['url']
        print("Done Get it")
        

        context = {
            'image' : image_url,
        }
        time.sleep(3)
    return render(request, 'main.html', context)  