# ✨ Git Commit Helper

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-orange?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Git 커밋 메시지를 더욱 **일관되고 효율적으로 작성**할 수 있도록 도와주는 커밋 메시지 도우미입니다.  
VSCode, Git Bash, GitHub Desktop 등 다양한 툴 환경에서 사용 가능한 포맷을 지원하며, 깔끔한 UI와 사용자 편의 기능을 제공합니다.

---

## 🖥️ 주요 기능

- 📌 **기본/커스텀 메시지 프리셋** 버튼
- 📝 제목/본문 입력란과 자동 포맷 구성
- 💡 `Tab`, `Shift+Tab`을 통한 하위 메시지 구조 정리
- 📋 `Ctrl+Z`, `Ctrl+Shift+Z`로 Undo/Redo 지원
- 🎨 다크 테마 UI (GitHub 스타일 감성)
- 📤 `복사하기` 버튼 클릭으로 git 명령 완성 & 클립보드 저장
- 🔁 다양한 커밋 포맷 지원:  
  - Git Bash  
  - VSCode  
  - GitHub Desktop  
  - 기본 (텍스트)

---

## 📦 설치 및 실행

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 실행
```bash
python main.py
```

### 3. 빌드 (Windows 전용)
```bash
pyinstaller --noconsole --onefile --icon=helper_icon.ico main.py
```

---

## 🗂️ 프로젝트 구조

```
GitCommitHelper/
│
├── gui.py              # 메인 GUI 실행 스크립트
├── clipboard.py        # 복사 기능 핸들러
├── formatter.py        # 본문 포맷 처리 (번호 등)
├── config.py           # 포맷 선택 저장
├── constants.py        # 메시지 프리셋, 아이콘 경로 등
├── theme.py            # UI 다크 테마 설정
├── utils.py            # 공통 유틸 함수
├── main.py             # 실행 진입점
├── helper_icon.ico     # 앱 아이콘
└── README.md           # 이 파일!
```

---

## 💬 커밋 메시지 예시

**Git Bash / VSCode 모드 예시**
```
git commit -m "[Feature] 🎯 25.06.24 Add new stage system" -m "1. Stage manager created
2. JSON loader added"
```

**GitHub Desktop 모드 예시**
```
제목: [Feature] 🎯 25.06.24 Add new stage system  
본문:
1. Stage manager created  
2. JSON loader added
```

---

## 📌 참고 사항

- 제목 또는 본문 중 하나만 있어도 자동 커밋 문구 생성
- 이모티콘 포함 가능 (폰트와 테마 고려함)
- 내부에 `"` 또는 `'` 포함된 경우 자동 이스케이프 처리
- 아이콘은 `.ico`로 지정, PyInstaller 시 같이 포함 필요

---

## 🧑💻 개발자

> 개발시간 단축을 위해 노력한 흔적입니다.
> 실전형 Git 커밋 내용 생성 도우미 툴입니다.
> 개선이 필요하면 언제든지 이슈를 남겨주세요! 🙌