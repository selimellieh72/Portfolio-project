from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
urlpatterns = [
    path('', jobs.views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
