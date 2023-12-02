from django.urls import path
from .views import HomePageView, UserDetailView, MessageView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/<int:id>', UserDetailView.as_view(), name='contact'),
    path('contact/<int:id>/message', MessageView.as_view(), name='message'),
]