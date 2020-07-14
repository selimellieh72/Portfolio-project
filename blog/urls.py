from blog import views
from django.urls import path
urlpatterns = [
    path('', views.allblogs, name = "blog"),
    path('<int:blog_id>', views.detailedblog, name = "detail")
]

