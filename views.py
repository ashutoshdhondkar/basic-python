from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import FileUploads
import pandas as pd
import os

# import openpyxl
# Create your views here.
def index(request):
    return render(request,'SortApp/index.html')


def validate(request):
    if(request.method == 'POST'):
        try:
            filepath = request.FILES['file']
        except Exception:
            return HttpResponse("Please select a file")
        else:
            sort_style = request.POST['sort_style']
            column_name = request.POST['column_name']
            
            print(f"sort style = {sort_style} and column name = {column_name}")
#             print(type(sort_style))
            print(filepath)
            
            
            # temporarily save file in db so that it gets updated in media folder
            obj = FileUploads(filepath = filepath)
            obj.save()
            
            # now once the file is stored in media folder, delete it from database
            obj.delete()
            
            # create a list of columns
            columns = []
            df = pd.read_excel(filepath)
            print(df.columns.values)
    #         name = input("Enter column name : ")
            try:
                for x in df.columns.values:
                    columns.append(x.strip())
            except Exception:
                pass
            print(columns)
            if(column_name in columns):
                # sort it on the basis of name
                
                # 1= ascending 2= descending
                if(sort_style == '1'):
                    df = df.sort_values([column_name],ascending = True)
                else:
                    df = df.sort_values([column_name],ascending = False)
                print(df)
                
    #             path_to_save = str(settings.MEDIA_ROOT)+'/files/'+filepath
    #             print(path_to_save)
    
                # save the file now in same location from where it is received
                df.to_excel(filepath,index=False)
                
                
                try:
                    obj = FileUploads(filepath = filepath)
                    obj.save()
                     
                except Exception as e:
                    print(e)
    #             obj = FileUploads(filepath = filepath)
    #             obj.save()
                context = {'obj' : obj}
                return render(request,'SortApp/home.html',context)
            else:
                return HttpResponse("Please specify proper column name")
            #return HttpResponse(filepath)

    return HttpResponse("Some Error")
     
