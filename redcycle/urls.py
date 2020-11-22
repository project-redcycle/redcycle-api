from django.urls import include, path
from rest_framework import routers
from .views.UserViewSet import *
from .views.LocationViewSet import *
from .views.CommunityPostViewSet import *
from .views.Signup import *

router = routers.DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/locations', LocationViewSet)
router.register(r'/communityPosts', CommunityPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('/account/', include('django.contrib.auth.urls')),
    path('/account/signup', Signup, name='signup'),
]
