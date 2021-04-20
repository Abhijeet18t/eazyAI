from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import TrainedModels
import json
import os


@csrf_exempt
def uploadModel(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        name = request.POST['modelName']
        extension = os.path.splitext(str(request.FILES['file']))[1]
        if(extension != '.pt'):
            return HttpResponse('Invalid File Type')
        data = TrainedModels.objects.values('modelName')
        for x in data.iterator():
            if(name == x["modelName"]):
                return HttpResponse('Model name already taken!')
        fs = FileSystemStorage('./media/ptFiles')
        newName = name+'.pt'
        filename = fs.save(newName, myfile)
        uploaded_file_url = fs.url(filename)
        print(filename, uploaded_file_url)
        trainedModels = TrainedModels(modelName=name, path=uploaded_file_url)
        trainedModels.save()
        return HttpResponse('Model Uploaded Successfully')


def listAll(request):
    data = TrainedModels.objects.values('modelName')
    listValues = []
    for x in data:
        listValues.append(x["modelName"])

    return HttpResponse(json.dumps(listValues))
