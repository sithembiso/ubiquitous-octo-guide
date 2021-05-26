from django.contrib import admin
from django.urls import path
from tasks.views import TaskView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks', TaskView.as_view()),
    path('', index)
]
