from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('oggabogga/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('', include('userauth.urls')),
]
