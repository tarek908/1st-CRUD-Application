from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.UploadPage, name='uploadpage'), 
    # path('show/', views.showPage, name='show'),
    path('upload/', views.upload_form, name='upload'),
    path('fatch/', views.fetch, name='fatch'),
    path('editpage/<int:pk>/', views.EditPage, name='editpage'),
    # path('editfatch/<int:pk>/', views.EditFatch, name='editfatch'),
    path('updata/<int:pk>/', views.upData, name='updata'),
    path('delete/<int:pk>/', views.Delete, name='delete')
]
