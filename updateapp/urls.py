from django.urls import path
from .views import userupdateView


urlpatterns=[
    path("update/student/<int:pk>/",userupdateView.as_view(),name='student-update'),
    #path("student/1/",studentupdate.as_view(),name='student-list-details'),
] 