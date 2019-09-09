from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from creation.models import TutorialResource,\
            TutorialDetail, FossSuperCategory,\
             FossCategory, TutorialCommonContent, TutorialDuration
from api.serializers import VideoSerializer, CategorySerializer, FossSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, F
import json
from django.conf import settings
from creation.views import get_video_info
import math


@csrf_exempt
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = TutorialResource.objects.filter(status=1, id=1)
        serializer = VideoSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_tutorial_list(request, fossid, langid):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        tuts = TutorialResource.objects.filter(language_id=langid,
                tutorial_detail_id__foss=fossid, status=1)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoSerializer(tuts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':

        data = JSONParser().parse(request)
        serializer = VideoSerializer(tut, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':

        tut.delete()
        return HttpResponse(status=204)


def show_categories(request):
    """
    List all categories.
    """
    if request.method == 'GET':
        categories = FossSuperCategory.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_fosslist(request):
    """
    Retrieve, fosslist based on category.
    """
    fosslist=[]
    if request.method == 'GET':
        fosses = FossCategory.objects.filter(
            status=1, show_on_homepage=1, available_for_nasscom=1).order_by('foss')
        for foss in fosses:
            fossdict={}
            tot_hour = 0
            tot_mins = 0
            tot_secs = 0
            tutorials = TutorialDuration.objects.filter(tutorial__foss=foss)
            for tutorial in tutorials:
                #print("tutorial :",tutorial.tutorial.foss,tutorial.tutorial,tutorial.duration)
                if len(tutorial.duration)>6:
                    hr,minutes,secs = tutorial.duration.split(':')                    
                    tot_hour += int(hr)
                    tot_mins += int(minutes)
                    tot_secs += int(secs)                    
                    #print('hr :',tot_hour,' mins : ',tot_mins,' secs: ',tot_secs)
            tot_mins += math.ceil(tot_secs/60)
            tot_hour = math.floor(tot_mins/60)
            timetotal = str(tot_hour) +'hr'+str(tot_mins%60)+'mins' 
            #print("\n\n\n")    
            all_keywords=""
            keywords = TutorialCommonContent.objects.filter(tutorial_detail__foss_id=foss.id)
            
            key_list = []
            for keyword in keywords:
                keys = keyword.keyword.split (",")                
                for k in keys:
                    if k not in key_list:
                        key_list.append(k)
            for category in foss.category.all():
                key_list.append(str(category))

            image_name = foss.foss.replace(' ', '-') + '.jpg'

            foss_image = "http://static.spoken-tutorial.org/images/"+image_name
            fossdict = {
            "course_id": foss.id,
            "title": foss.foss,
            "duration": timetotal,
            "metadata": foss.description,
            "price":"Free",
            "currency":"",
            "content_type":"course",
            "deeplink_url":"https://spoken-tutorial.org/tutorial-search/?search_foss="+foss.foss+"&search_language=English",
            "image_url":foss_image,
            "description":foss.description,
            "keywords":key_list
            }          
            fosslist.append(fossdict)
        
        fosslist = json.dumps(fosslist)
        # serializer = FossSerializer(fosslist, many=True)        
        #return JsonResponse(serializer.data, safe=False)
        return HttpResponse(fosslist, content_type='application/json')