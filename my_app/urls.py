from django.urls import path
from . import views

urlpatterns = [

    path('',views.log_In,name='log_In'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('otp_page/',views.otp_verify,name='otp_page'),
    path('index/',views.index,name='index'),
    path('my_account/',views.my_account,name='my_account'),
    path('forgot_password_1/',views.forgot_password_1,name="forgot_password_1"),
    path('forgot_password_2/',views.forgot_password_2,name="forgot_password_2"),
    path('forgot_password_3/',views.forgot_password_3,name="forgot_password_3"),
    path('upload_media/',views.upload_media,name='upload_media'),
    path('view_video/',views.view_video,name='view_video'),
    path('notification/',views.notification,name='notification'),
    path('categories/',views.categories,name='categories'),
    path('add_notification/',views.add_notification,name='add_notification'),
    path('filter/',views.filter,name='filter'),
    path('liked/<int:pk>', views.like_video, name = 'like'),
    path('report/<int:pk>', views.report_video, name = 'report'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('toprated/',views.toprated,name='toprated'),
    path('like_contact/<int:pk>',views.like_contact,name='like_contact'),
    path('message/',views.message,name='message'),
]