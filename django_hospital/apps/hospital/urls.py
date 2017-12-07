# from django.conf.urls.static import static
from django.conf.urls import patterns, url
# from django.conf import settings

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^generate/doctor/$', views.generate_doctor),
    url(r'^generate/nurse/$', views.generate_nurse),
    url(r'^generate/patient/$', views.generate_patient),
    url(r'^generate/dbadmin/$', views.generate_dbadmin),
    url(r'^generate/visit/$', views.generate_visit),
    url(r'^generate/med_price/$', views.generate_med_price),
    url(r'^generate/prescription/$', views.generate_prescription),
    url(r'^generate/vaccine/$', views.generate_vaccine_applied),
    url(r'^generate/assign_doctors/$', views.assign_doctors),

    url(r'^generate/groups/$', views.generate_groups),
    url(r'^generate/specialities/$', views.generate_specialities),
    url(r'^generate/meds/$', views.generate_meds),
    url(r'^generate/vaccines/$', views.generate_vaccines),
    url(r'^generate/departments/$', views.generate_departments),
    url(r'^generate/$', views.generate),
)

