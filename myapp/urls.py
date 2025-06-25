from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_list,name='task_list'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # ✅ Make sure this exists
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),  # ✅ This is required
]
# urlpatterns = [
#     path('', views.task_list, name='task_list'),
# ]