"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from mobile.views import MobileViews,MobileDetailsView
from mobapi import views as apiview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/teq/mobiles/",apiview.MobileView.as_view()),
    path("api/v1/teq/mobiles/<int:id>",apiview.MobileDetailsView.as_view()),
    path("api/v2/teq/mobiles/",apiview.MobileModelView.as_view()),
    path("api/v2/teq/mobiles/<int:id>",apiview.MobileModelDetailsView.as_view())
    # path('morning/',views.GoodMorningView.as_view()),
    # path('evening/',views.GoodEveningView.as_view()),
    # path('hello/',views.HelloView.as_view()),
    # path('noon/',views.NoonView.as_view()),
    # path('add/',views.AddView.as_view()),
    # path('sub/',views.SubstractionView.as_view()),
    # path('mul/',views.MultiplicationView.as_view()),
    # path('qube/',views.QubeView.as_view()),
    # path('fact/',views.FactorialView.as_view()),
    # path('prime/',views.PrimeNumberView.as_view()),
    # path('api/v1/mobiles/',MobileViews.as_view()),
    # path('api/v1/mobiles/<int:id>',MobileDetailsView.as_view()),
]
