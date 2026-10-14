# Pitch Shape

포심 패스트볼의 수평·수직 무브먼트와 투수별 주요 보조 구종을 비교하는 소형 탐색 연구입니다.

```text
data/raw/stats.csv                       원본 입력
scripts/analyze_pitch_shape.py           실행 코드
outputs/tables/data.html                 HTML 데이터표
outputs/figures/pitch_shape_scatter.png  생성 그래프
archive/requirements.txt                 기존 환경 기록
```

## 실행

```powershell
python -m pip install -e .
python scripts/analyze_pitch_shape.py
```

## Windows 가상환경

이 폴더 전용 Python 3.12 `.venv`와 의존성을 구성했습니다. PowerShell에서 사용합니다.

```powershell
Set-Location '<BASEBALL_ROOT>\01_Research\07_Pitch_Shape'
. .\.venv\Scripts\Activate.ps1
python -m pip check
```

활성화 없이 `.\.venv\Scripts\python.exe`로 실행할 수도 있습니다.
VS Code에서는 이 프로젝트 폴더를 열고 `.venv` 인터프리터/노트북 커널을 선택합니다.
`requirements-windows.txt`는 Windows 의존성, `requirements-windows.lock.txt`는 실제 설치 버전입니다.
환경 재생성은 이 프로젝트 폴더에서 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-windows.txt
```

새 환경의 로컬 모듈 경로 등록은 [공통 환경 설정](../../README.md#프로젝트별-환경-설정)을 따릅니다.

## 폴더 구성

| 경로 | 역할 |
|---|---|
| `archive/` | 과거·보관 코드와 기록 |
| `data/` | 프로젝트 입력·파생 데이터 |
| `outputs/` | 생성 결과·모델·보고서 |
| `scripts/` | 실행 스크립트 |
| `README.md` | 폴더 구조·실행 안내 |
| `AGENTS.md` | 코드 작성·변경·검증 규칙 |
