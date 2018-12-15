from django.conf.urls import url, include
from rest_framework import routers
from blog.api_service import views

router = routers.DefaultRouter()
router.register(r'/posts', views.PostViewSet)
router.register(r'/posts/ordered', views.OrderedPostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]