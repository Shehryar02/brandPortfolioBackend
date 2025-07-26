from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, EmailFooterViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet)
router.register(r'footerEmail', EmailFooterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
