from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    # 1. Admin Page
    path('admin/', admin.site.urls),
    
    # 2. Signup & Login
    path('', views.register_user, name='home'), 
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    
    # 3. Profile & Assessment
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('assessment/', views.assessment_view, name='assessment'),
    
    # 4. Dashboard Logic
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # 5. Activity Tracking
    path('add-activity/', views.add_activity, name='add_activity'),
]