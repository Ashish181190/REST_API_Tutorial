from django.db import models

# Create your models here.


class Tutorial(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


        
        
        ser= TutorialSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    