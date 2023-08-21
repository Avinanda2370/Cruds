from django.urls import path
from .views import home, update, create, SEE_PROF, delete

urlpatterns = [
    path('', home, name='home'),
    path('update/<int:id>/', update, name='update'),
    path('create/', create, name='create'),
    path('see_prof/<int:id>/',SEE_PROF, name='see_prof'),
    path('delete/<int:id>/',delete, name='delete'),
]
