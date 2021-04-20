from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, HttpResponseBadRequest)
import os
import json


def index(request):
    # detect('media/ptFiles/best.pt', 'media/img/pen.jpg',
    # 614, 0.25, 0.45, 0, 'cpu', 'res.jpg', 'res.txt')
    return HttpResponse("Welcome to eazyAI")


@ csrf_exempt
def upload(request):
    if request.method == 'POST':
        myfile = request.FILES['image']
        extension = os.path.splitext(str(request.FILES['image']))[1]
        print('extension==' + extension)
        if(extension not in ['.jpg', '.png', '.jpeg']):
            return HttpResponse(0)
        modelType = request.POST['modelName']
        weightsPath = 'media/ptFiles/'+modelType+'.pt'
        fs = FileSystemStorage('./media/img')
        filename = fs.save(myfile.name, myfile)
        imgPath = 'media/img/'+filename
        # pass values to Detect function here
        cmd = f"python D:/work/KMITL/eazyAI/BE+AI/AI/detect.py --source {imgPath} --weights {weightsPath}  --conf 0.25"
        os.system(cmd)
        return HttpResponse(filename)


def success(request):
    return HttpResponse('successfully uploaded')
