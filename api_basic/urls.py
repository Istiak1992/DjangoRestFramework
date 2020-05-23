from django.urls import path, include
from . import views
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, GenericArticleViewSet, ModelArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('article', ArticleViewSet, basename='article')
#router.register('article', GenericArticleViewSet, basename='article')
router.register('article', ModelArticleViewSet, basename='article')

urlpatterns = [
    #path('', views.article_list, name='article_list'),
    #path('detail/<int:pk>/', views.article_detail, name='detail'),
    path('', ArticleAPIView.as_view(), name='article_list'),
    path('detail/<int:pk>/', ArticleDetails.as_view(), name='detail'),
    path('generic/', GenericAPIView.as_view(), name='generic_article_list'),
    path('generic/<int:pk>/', GenericAPIView.as_view(), name='generic_article_list'),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
   
]

