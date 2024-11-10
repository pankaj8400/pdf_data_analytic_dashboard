# violation/urls.py


from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('no-violation/', login_required(views.no_violation), name='no_violation'),
    path('generate-report/', views.generate_pdf, name='generate_pdf'),
    path('generate-record/', views.generate_record, name='generate_record'),
    path('view-violations/', views.view_violations, name='view_violations'),
    path('settings/', login_required(views.user_settings), name='help'),
    path('download_csv/',views.download_csv, name='download_csv'),
    path('logout/', views.logout_view, name='logout'),
]
