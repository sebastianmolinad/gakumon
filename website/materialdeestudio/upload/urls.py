from django.urls import path


from .views import HomePageView, UploadFile

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('upload/', UploadFile.as_view(), name='upload_file')
]

