from django.urls import include, path
from ingredients.views import IngredientsViewSet
from recipes.views import RecipesViewSet
from rest_framework.routers import DefaultRouter
from tags.views import TagsViewSet
from users.views import UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('recipes', RecipesViewSet)
router_v1.register('tags', TagsViewSet)
router_v1.register('ingredients', IngredientsViewSet)
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router_v1.urls)),
]
