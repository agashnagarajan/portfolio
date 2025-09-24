from django.contrib import admin
from django.urls import path
from myapp import views
# from .views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('contact/', contact_view, name='contact'),
]
