from django.shortcuts import render
from rest_framework import generics 
from updateapp.models import update
from updateapp.serializers import updateserializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from updateapp.utils import api_response

@method_decorator(csrf_exempt, name="dispatch")
class userupdateView(generics.ListCreateAPIView):
    queryset = update.objects.all()
    serializer_class = updateserializers

    def put(self, request, *args, **kwargs):
        # Get the data from the request
        student_data = request.data
        
        # Ensure 'sno' is provided in the data
        sno = student_data.get('sno')
        if sno is None:
            # If 'sno' is missing, return an error response
            return api_response(400, 'Error: Missing sno in request data', {})
        instance=self.get_object()
        
        # Update the student instance 
        instance.sno = sno
        instance.student = student_data.get('student')
        instance.classroom = student_data.get('classroom')
        instance.save()
        
        # Access the updated student's attributes correctly
        updated_student_name = instance.student
        
        # Return the response with the updated student's information
        return api_response(200, 'Successfully updated. Please check once', {"updated_student": updated_student_name})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






































# class student(generics.ListCreateAPIView) :
#     queryset=update.objects.all()
#     serializer_class=updateserializers
    
# class studentupdate(generics.RetrieveUpdateDestroyAPIView):    
    
#     queryset=update.objects.all()
#     serializer_class=updateserializers    
    
    
    
# Create your views here.
