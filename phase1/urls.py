from django.conf.urls import url
from phase1 import views

urlpatterns = [
    url(r'^home/', views.TestAPI.as_view(), name='get-home-page-data'),
    url(r'^runcode/', views.RunPythonCode.as_view(), name='runcode'),
]
