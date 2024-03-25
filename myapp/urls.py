from django.urls import path
from . import views 
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
   
    path('delete_all_data1/', views.delete_all_data1, name='delete_all_data1'),
    path('delete_all_data2/', views.delete_all_data2, name='delete_all_data2'),
    path('delete_all_data3/', views.delete_all_data3, name='delete_all_data3'),
    path('delete_all_data4/', views.delete_all_data4, name='delete_all_data4'),
    # عرض الصفحة الرئيسية التي تحتوي على طلبات الطلاب
    path('1/', views.show_requests1, name='show_requests1'),

    # تنفيذ عملية القبول
    path('accept_request/<int:request_id>/', views.accept_request1, name='accept_request1'),
    # تنفيذ عملية الرفض
    path('reject_request/<int:request_id>/', views.reject_request1, name='reject_request1'),
    path('2/', views.show_requests2, name='show_requests2'),
    path('accept_request2/<int:request_id>/', views.accept_request2, name='accept_request2'),
    path('reject_request2/<int:request_id>/', views.reject_request2, name='reject_request2'),
    path('3/', views.show_requests3, name='show_requests3'),
    path('accept_request3/<int:request_id>/', views.accept_request3, name='accept_request3'),
    path('reject_request3/<int:request_id>/', views.reject_request3, name='reject_request3'),
       path('4/', views.show_requests4, name='show_requests4'),
    path('accept_request4/<int:request_id>/', views.accept_request4, name='accept_request4'),
    path('reject_request4/<int:request_id>/', views.reject_request4, name='reject_request4'),




    path('2/', views.ce_2, name='ce_2'),
    path('3/', views.ce_3, name='ce_3'),
    path('4/', views.ce_4, name='ce_4'),
    path('5/', views.ce_5, name='ce_5'),
    
    
    path('les1/', views.less, name='les1'),
    path('les2/', views.less1, name='les2'),
    path('les31/', views.less31, name='les31'),
    path('les32/', views.less32, name='les32'),
    path('les41/', views.less41, name='les41'),
    path('les42/', views.less42, name='les42'),
    path('done/', views.done_view, name='done_view'),
    path('elc/', views.elc, name='elc'),
    path('elc1/', views.elc1, name='elc1'),
    path('stage/', views.stage, name='stage'),
    path('stagecyber/', views.stagecyber, name='stagecyber'),
    
    path('comp1/', views.comp1, name='comp1'),
        path('comp2/', views.comp2, name='comp2'),

    
    path('lap1/', views.lap1, name='lap1'),
    path('lap2/', views.lap2, name='lap2'),
    path('lap3/', views.lap3, name='lap3'),
    path('lap32/', views.lap32, name='lap32'),
    path('lap4/', views.lap4, name='lap4'),
    path('lap42/', views.lap42, name='lap42'),
    path('les1cyber/', views.les1cyber, name='les1cyber'),
    path('lap1cyber/', views.lap1cyber, name='lap1cyber'),
    
    
re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name='404'),
]