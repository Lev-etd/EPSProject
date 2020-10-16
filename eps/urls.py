from django.urls import path
# from .views import Start, Yur, Fiz, Corp
from eps import views

urlpatterns = [
    #     path('', Start.as_view(), name='start-page'),
    #     path('yur', Yur.as_view(), name='yur'),
    #     path('fiz', Fiz.as_view(), name='fiz'),
    #     path('corp', Corp.as_view(), name='corp')
    path('', views.start, name='start-page'),
    path('yur', views.yur, name='yur'),
    path('fiz', views.fiz, name='fiz'),
    path('corp', views.corp, name='corp'),
    path('dbo_list_fiz', views.resultfiz, name='dbo_list_fiz'),
    path('dbo_list_yur', views.resultyur, name='dbo_list_yur'),
    path('dbo_list_corp', views.resultcorp, name='dbo_list_corp'),
]
