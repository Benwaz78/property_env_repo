from django.urls import path
from public_view import views
app_name ='public_view'
urlpatterns = [
    path('about-page', views.about, name='about'),
    path('detail-about/<int:team_id>', views.detail_about, name='detail_about'),
    path('agent-page', views.agent, name='agent'),
    path('rent-page', views.rent, name='rent'),
    path('requests-page', views.request, name='request'),
    path('property-details/<slug:slug>/<int:category_id>', views.property_details, name='property_details'),
    path('buy-page', views.buy, name='buy'),
    path('register-page', views.register, name='register'),
    path('login-page', views.login_view, name='login_view'),
]
