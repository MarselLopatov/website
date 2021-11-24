from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.post, name='post'),
    path('<int:pk>/update', views.UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='delete_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
