from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^information/$',views.update_information,name='information'),
]
