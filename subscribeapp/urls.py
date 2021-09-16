from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name='subscribeapp'
urlpatterns= [
    path('subscribes/', SubscriptionView.as_view(), name='subscribes'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]