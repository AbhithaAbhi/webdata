from django.urls import path
from . import views
from performance.views import chart_page
urlpatterns = [
    path('employee-performance/', views.EmployeePerformanceList.as_view(), name='employee-performance-list'),
    path('', views.chart_page , name='chart_page'),
]
