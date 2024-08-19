
from django.urls import path,include
from 

# Define the URL patterns
urlpatterns = [
    path('master/',op)
    path('api/createrole/', create_role_view, name='roleregister'),  # Assuming create_role_view is defined elsewhere
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
