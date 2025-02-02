from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, FAQListView

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view/', FAQListView.as_view(), name='faq-list'),
]
