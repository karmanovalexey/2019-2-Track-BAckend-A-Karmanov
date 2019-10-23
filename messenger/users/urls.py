from users.views import user_profile, user_contacts
from django.urls import path

urlpatterns = [path('', user_profile, name='user_profile'),
                path('contacts/', user_contacts, name='user_contacts')]
