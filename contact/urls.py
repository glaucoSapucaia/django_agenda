from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # contact.forms urls
    path('create/', views.create, name='create'),

    # contact.views urls
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
