"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
#from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from product import views
#from order import views


router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'purchase', views.PurchaseViewSet)
#router.register(r'order', views.OrderViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include(router.urls)),
   # url(r'^order/', include(router.urls)),
   
]
