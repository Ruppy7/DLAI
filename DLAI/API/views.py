from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from . import tesseract_text
# Create your views here.

class FileUploadAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request):
        uploaded_file_serialized = UploadedFileSerializer(data=request.data)
        if uploaded_file_serialized.is_valid():
            uploaded_file_serialized.save()
            uploaded_file = uploaded_file_serialized.instance
            if uploaded_file.file.name.endswith(('.png', '.jpg')):
                file_path = uploaded_file.file.path
                extracted_data = tesseract_text.extract_from_file(uploaded_file.file.name,file_path)
                uploaded_file.delete()
                return Response({'success' : extracted_data}, status = status.HTTP_200_OK)
            else:
                uploaded_file.delete()
                return Response({'error': 'uploaded file must be an image'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            uploaded_file.delete()
            return Response(uploaded_file_serialized.errors, status= status.HTTP_400_BAD_REQUEST)
        
def upload_pdf(request):
    return render(request, 'index.html')
