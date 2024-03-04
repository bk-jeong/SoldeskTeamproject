from django.contrib import admin
from django.urls import path, re_path
from loaTier import views
from django.conf import settings

from django.views.static import serve



handler400 = 'loaTier.views.error400'
handler404 = 'loaTier.views.error404'
handler500 = 'loaTier.views.error500'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path('make/<str:group>/', views.make, name='tierMaker'),
    path('res/<str:group>/<str:id>', views.personal, name="userResult"),
    path('res/all/', views.statitcs, name="allResult"),
    re_path(r'^static/(?P<path>.*)', serve, kwargs={'insecure': True}),
]
