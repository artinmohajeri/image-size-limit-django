from django.shortcuts import render
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse
from django.http import JsonResponse
import json
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.csrf import csrf_exempt

obj=None
size, dimentions = "", ""

def upload(request):
    global obj, size, dimentions
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Image(img = form.cleaned_data["file"])
            obj.save()
    else:
        form = ImageForm()
        if not obj:
            size = ""
            dimentions = ""     
    return render(request, 'upload.html', {"form":form, 'obj':obj,'size':size, 'dimentions':dimentions})


@csrf_exempt
def my_ajax_view(request):
    global size, dimentions
    if request.method == 'POST':
           data_from_js = json.loads(request.body)
           my_js_variable = data_from_js['data']
           print(my_js_variable)
           size = my_js_variable["s"]
           dimentions = my_js_variable["d"]
           print(size)
           print(dimentions)
           return JsonResponse({'message': 'Data received successfully'})
