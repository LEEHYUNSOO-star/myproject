# ppt_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # /run_streamlit/ URL로 요청이 들어오면 run_streamlit 뷰 함수 실행
    path('run_streamlit/', views.run_streamlit, name='run_streamlit'),
]
