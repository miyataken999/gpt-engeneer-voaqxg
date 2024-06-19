from django.urls import include, path

urlpatterns = [
    path('wallet/', include('wallet.urls')),
]