from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

## for view image
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.home,  name='home'),
    url(r'^edit_home$', views.edit_home,  name='edit_home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/', include('register_app.urls') ),
    url(r'^data/', include('data.urls') ),
    url(r'^reports/', include('reports.urls') ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)