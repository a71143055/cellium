# Cellium

Cellium — 세포 기반 메타러닝 하드웨어 설계 플랫폼 (Prototype)

## 개요
이 저장소는 Cellium 윈도우 앱의 프로토타입 구현입니다.
Python(PySide6) GUI와 C++ 시뮬레이션 백엔드를 포함합니다.

## 요구사항
- Windows 10/11
- Python 3.10+
- Visual Studio (C++ 빌드 도구) 또는 MSVC
- CMake
- pip packages: see requirements.txt

## 설치 (개발용)
1. 가상환경 생성:
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
