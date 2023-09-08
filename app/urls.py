from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('trainer_register', views.trainer_register, name='trainer_register'),
    path('trainer_panel', views.trainer_panel, name='trainer_panel'),
    path('login_view', views.login_view, name='login_view'),
    path('login', views.login, name='login'),
    path('trainer_view', views.trainer_view, name='trainer_view'),
    path('trainer_update/<int:id>', views.trainer_update, name='trainer_update'),
    path('trainer_delete/<int:id>', views.trainer_delete, name='trainer_delete'),
    path('customer_register', views.customer_register, name='customer_register'),
    path('customer_panel', views.customer_panel, name='customer_panel'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('customer_view_customer', views.customer_view_customer, name='customer_view_customer'),
    path('trainer_view_trainer', views.trainer_view_trainer, name='trainer_view_trainer'),
    path('add_attendance', views.add_attendance, name='add_attendance'),
    path('mark/<int:id>', views.mark, name='mark'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('day_attendance/<date>', views.day_attendance, name='day_attendance'),
    path('view_attendance_user', views.view_attendance_user, name='view_attendance_user'),
    path('log_out_view', views.log_out_view, name='log_out_view'),
    path('profile', views.profile, name='profile'),








]
