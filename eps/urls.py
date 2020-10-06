from django.urls import path
from .views import Start, Yur, Fiz, Corp

urlpatterns = [
    path('', Start.as_view(), name='start-page'),
    path('yur', Yur.as_view(), name='yur'),
    path('fiz', Fiz.as_view(), name='fiz'),
    path('corp', Corp.as_view(), name='corp')
    # path('', views.yur, name='yur'),
    # path('', views.fiz, name='fiz'),
    # path('', views.corp, name='corp')
]
