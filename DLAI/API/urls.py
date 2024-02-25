from django.urls import path
from .views import FileUploadAPIView, upload_pdf

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view()),
    path('', upload_pdf),
]

