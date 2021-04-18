from django.urls import path
from public_view import views
app_name ='public_view'
urlpatterns = [
    path('about-page', views.about, name='about'),
    path('detail-about/<int:team_id>', views.detail_about, name='detail_about'),
    path('agent-page/', views.agent, name='agent'),
    path('rent-page/', views.rent, name='rent'),
    path('requests-page/', views.requests, name='requests'),
    path('filter-data/', views.filter_form, name='filter_form'),
    path('property-details/<slug:slug>/<int:category_id>/<int:prop_id>/', views.property_details, name='property_details'),
    path('buy-page/', views.buy, name='buy'),
    path('login-page/', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-property/', views.add_property, name='add_property'),
    path('add-location/', views.add_location, name='add_location'),
     path('view-property-byagent/', views.view_property_byagent, name='view_property_byagent'),
    # path('confirm-logout/', views.confirm_lsogout, name='confirm_logout'),
    path('logout-page/', views.logout_view, name='logout_view'),
]
