from django.contrib import admin
from django.conf import settings # new
from django.conf.urls.static import static # new

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portfolio.urls')),
    path('',include('blog.urls')),
]
