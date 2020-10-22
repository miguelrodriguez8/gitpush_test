from django.urls import path
# from .views import view_function
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('', view_function, name="home"),
    path('', HomePageView.as_view(), name="home"),
    # path('', HomePageView.as_view(), name="home/aboutme"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)