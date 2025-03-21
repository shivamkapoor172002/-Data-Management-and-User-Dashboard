from django.contrib import admin
from django.urls import path
from record import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('statusrecord/', views.status_record, name='statusrecord'),
    path('update_record/', views.update_record, name='update_record'),
    
    # New or updated paths
    path('validate/', views.validate_data, name='validate_data'),
    path('simplified_data/', views.simplified_data, name='simplified_data'),
    path('update_simplified_data/', views.update_simplified_data, name='update_simplified_data'),
    path('delete_simplified_data/', views.delete_simplified_data, name='delete_simplified_data'),
    path('get_simplified_data/', views.get_simplified_data, name='get_simplified_data'),
    path('summarized_monthly_data/', views.summarized_monthly_data, name='summarized_monthly_data'),
    path('user-data/', views.user_data, name='user_data'),




]