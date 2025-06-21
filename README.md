# ✨ Git Commit Helper

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-orange?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Git 커밋 메시지를 더욱 **일관되고 효율적으로 작성**할 수 있도록 도와주는 커밋 메시지 도우미입니다.  
VSCode, Git Bash, GitHub Desktop 등 다양한 툴 환경에서 사용 가능한 포맷을 지원하며, 깔끔한 UI와 사용자 편의 기능을 제공합니다.

---

## 🖥️ 주요 기능

- 📌 커밋 메시지 프리셋 버튼으로 빠른 제목 구성
- 📝 본문 번호 자동 정렬 (`Tab`, `Shift+Tab`)
- 💡 Undo/Redo 지원 (`Ctrl+Z`, `Ctrl+Shift+Z`)
- 📤 복사하기 버튼으로 **`git commit` 명령 복사**
- 🌓 GitHub 스타일 다크 테마 지원
- 🔁 다양한 포맷 지원 (Git Bash / VSCode / GitHub Desktop / 일반 텍스트)
- 🌐 **언어 변경 기능 (한국어/영어)**
- 📋 **줄바꿈 표현 포함된 커맨드 복사 최적화**
- 🪵 **로깅 기능 추가 (app.log)**

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

### 3. 빌드 (Windows)
```bash
pyinstaller --noconfirm --windowed --icon=assets/helper_icon.ico main.py
```

빌드 후 생성된 `dist/CommitHelper.exe` 파일을 실행하세요.

---

## 🗂️ 프로젝트 구조

```
GitCommitHelper/
├── assets/
│   ├── helper_icon.ico
│   └── helper_icon.png
│
├── config/
│   ├── app_config.py
│   ├── constants.py
│   └── i18n.py
│
├── core/
│   ├── clipboard.py
│   ├── undo_stack.py
│
├── events/
│   └── event_handler.py
│
├── gui/
│   └── window.py
│
├── ui/
│   ├── auto_scrollbar.py
│   ├── theme.py
│   └── ThemeTest/
│       ├── darkmode.py
│       ├── github.py
│       └── light_mode.py
│
├── utils/
│   ├── asset_loader.py
│   ├── formatter.py
│   └── logger.py
│
├── main.py
├── README.md
```

---

## 💬 커밋 메시지 복사 예시

**Git Bash / VSCode 모드 복사 예시**
```
git commit -m "[Refact] ♻️ 22.06.25" -m "
1. asdf\\n
1.1. subtask\\n
2. next line\\n
"
```

**복사된 메시지는 줄바꿈이 시각적으로 확인 가능**하며,  
실제 커밋 시에도 그대로 적용됩니다 ✅

---

## 🛠 로깅 시스템

- 모든 주요 이벤트는 `app.log`에 저장됩니다.
- 복사 성공/실패, 버튼 클릭 등 디버깅에 유용한 정보를 자동 기록합니다.

```
2025-06-22 13:42:10 [INFO] git 명령 복사 성공
2025-06-22 13:42:11 [WARNING] pyperclip 실패 → tkinter fallback
```

---

## 📌 참고 사항

- 제목/본문 중 하나만 있어도 커밋 메시지 생성됨
- 이모지 포함 가능
- `"` `'` 자동 이스케이프 처리
- pyperclip 실패 시 자동으로 tkinter 클립보드로 전환

---

## 👨‍💻 개발자 메시지

> 이 프로젝트는 실제 커밋 작성의 반복을 줄이기 위해 제작된 유틸리티입니다.  
> 직관적이고 실용적인 기능에 집중했으며, 지속적인 개선을 계획 중입니다.