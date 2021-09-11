import tutorials
from django.shortcuts import render
from tutorials.serializers import TutorialSerializer
from tutorials.models import Tutorial
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == "GET":
        tutorials = Tutorial.objects.all()
        # print(tutorials)

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains = title)
        ser = TutorialSerializer(tutorials, many = True)

        return JsonResponse(ser.data, safe=False)

    elif request.method == "POST":  
        data = request.data
        # data = JSONParser().parse(request)
        # print(data)
        ser = TutorialSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(({'message': 'Data inserted successfully!'},ser.data), safe= False, status=status.HTTP_201_CREATED)
        return JsonResponse(ser.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(id = pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The Tutorial Does not exist...!'})

    if request.method == "GET":
        ser = TutorialSerializer(tutorial)
        return JsonResponse(ser.data)


    elif request.method == "PUT":
        ser = TutorialSerializer(tutorial, data= request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(({'message': 'Data Updated successfully!'}, ser.data), safe= False, status=status.HTTP_200_OK)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == "DELETE":
        tutorial.delete()
        return JsonResponse({'message': " Your data deleted successfully "})

@api_view(["GET"])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.all().filter(published= True)
    if request.method == "GET":
        ser = TutorialSerializer(tutorials, many= True)
    return JsonResponse(ser.data, safe= False)