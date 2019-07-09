from django.shortcuts import render
import requests
import os
import xlsxwriter
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from utils.excel_opration import Excel


def home(request):
    template = 'uploadexcel.html'
    return render(request, template)


def get_excel_op_object():
    return Excel()


def getExcel(request):
    if request.method == 'POST' and request.FILES:
        try:
            current_dir = os.path.abspath(os.path.dirname(__file__))
            BASE_DIR = os.path.abspath(current_dir + "/../")
            EXCEL_DIR = os.path.join(BASE_DIR, 'static')

            if not os.path.exists(EXCEL_DIR):
                os.makedirs(EXCEL_DIR)

            myfile = request.FILES['files']
            fs = FileSystemStorage(location=EXCEL_DIR)
            filename = fs.save(myfile.name, myfile)
            request_file_location = os.path.join(EXCEL_DIR, filename)
            excel_obj = get_excel_op_object()
            excel_obj.readDataFromExcel(
                request_file_location)  # precossing excel file
            download_file_link = '/static/' + filename

            return JsonResponse({'link': download_file_link})
        except Exception as e:
            print("Error in views module ", e)

    template = 'uploadexcel.html'
    return render(request, template)
