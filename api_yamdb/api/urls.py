
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet
from .views import UserViewSet, signup, get_token


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='token')
]


