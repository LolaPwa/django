
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from john import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('john.urls')),
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact")
    #path('send_mail', views.send_mail, name="send_mail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
