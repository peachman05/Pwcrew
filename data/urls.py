from django.conf.urls import url


from . import views

app_name = 'data'
urlpatterns = [
    url(r'^personal_info/(?P<user_id_input>[0-9]+)?', views.personal_info,  name='personal_info'),
    url(r'^address/(?P<user_id_input>[0-9]+)?', views.address,  name='address'),
    url(r'^work_info/(?P<user_id_input>[0-9]+)?', views.work_info,  name='work_info'),
    url(r'^insignia/(?P<user_id_input>[0-9]+)?', views.insignia,  name='insignia'),
    url(r'^education/(?P<user_id_input>[0-9]+)?', views.education,  name='education'),


    url(r'^list_teacher/', views.list_teacher,  name='list_teacher'),
    url(r'^delete_teacher/(?P<user_id_input>[0-9]+)?', views.delete_teacher,  name='delete_teacher'),

    url(r'^add_insignia/(?P<user_id_input>[0-9]+)?', views.add_insignia,  name='add_insignia'),
    url(r'^edit_insignia/(?P<insignia_id_input>[0-9]+)?', views.edit_insignia,  name='edit_insignia'),
    url(r'^delete_insignia/(?P<insignia_id_input>[0-9]+)?', views.delete_insignia,  name='delete_insignia'),

    url(r'^reset_password/(?P<user_id_input>[0-9]+)?', views.reset_password,  name='reset_password'),
    url(r'^change_username/(?P<user_id_input>[0-9]+)?', views.change_username,  name='change_username'),

]
