# ppt_app/views.py

import subprocess
from django.http import HttpResponse

# Streamlit 앱을 실행하는 뷰 함수
def run_streamlit(request):
    # Streamlit 앱 실행
    subprocess.run(["streamlit", "run", "ppt_app/streamlit_app.py"])  # Streamlit 앱 경로
    return HttpResponse("Streamlit 앱이 실행되었습니다.")
