from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'',views.AttendanceLogsView)

app_name = 'attendance'
urlpatterns = [
    path('',include(router.urls)),
]
