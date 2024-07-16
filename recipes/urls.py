from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
# from .views import RecipeViewSet

# router = DefaultRouter()
# router.register(r'recipes', RecipeViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('recipes/', views.RecipeList.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view())
]
