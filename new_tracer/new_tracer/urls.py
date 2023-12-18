"""
URL configuration for new_tracer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import UserViewSet
from utils.image_code import ImageView
from project.views import ProjectViewSet, ProjectUserViewSet, ProjectStarViewSet, ProjectUserStarViewSet, \
    AllProjectViewSet
from wiki.views import WikiViewSet
router = DefaultRouter()

router.register(r'users', UserViewSet, basename="user")
router.register(r'project', ProjectViewSet, basename="project")
router.register(r'projectuser', ProjectUserViewSet, basename="projectuser")
router.register(r'projectstar', ProjectStarViewSet, basename="project_star")
router.register(r'projectuserstar', ProjectUserStarViewSet, basename="projectuser_star")
router.register(r'projectall', AllProjectViewSet, basename="projectall")

router_manage = DefaultRouter()
router_manage.register(r'dashborad', ProjectViewSet, basename="dashborad")
router_manage.register(r'wiki', WikiViewSet, basename="wiki")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('manage/<int:project_id>/', include(router_manage.urls)),
    # drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    # jwt认证接口
    path('login/', obtain_jwt_token),
    path('captcha/', include('captcha.urls')),
    path('images/', ImageView.as_view())
]
