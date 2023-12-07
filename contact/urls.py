from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # contact.forms urls
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),

    # contact.views urls
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
