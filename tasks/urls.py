from django.urls import path 
from .views import (
    task_update, task_toggle,
    task_delete, task_list
)


app_name = "taskapp"
urlpatterns = [
    path("", task_list, name="task_list"),
    path("update/<int:pk>/", task_update, name="task_update"),
    path("toggle/<int:pk>/", task_toggle, name="task_toggle"),
    path("delete/<int:pk>/", task_delete, name="task_delete"),
    
]
