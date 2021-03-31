from django.urls import path
from backend import views
app_name ='backend'
urlpatterns = [
    path('hello', views.greet, name='greet' ),
    path('admin-page', views.index, name='index' ),
    # path('message-page', views.message, name='message'),

    path('addlist-page', views.addlistings, name='addlistings'),
    path('viewlist-page', views.view_list, name='view_list'),
    path('editlist-page', views.edit_list, name='edit_list'),
    # path('addlocation-page', views.add_location, name='add_location'),

    path('userprofile-page', views.user_profile, name='user_profile'),
    path('editprofile-page', views.edit_profile, name='edit_profile'),
    path('viewprofile-page', views.view_profile, name='view_profile'),

    path('addlocation-page', views.add_location, name='add_location'),
    path('editlocation-page', views.edit_location, name='edit_location'),
    path('viewlocation-page', views.view_location, name='view_location'),

    path('addproperty-page', views.add_property, name='add_property'),
    path('editproperty-page', views.edit_property, name='edit_property'),
    path('viewproperty-page', views.view_property, name='view_property'),

    path('change-password', views.change_password, name='change_password'),
]
