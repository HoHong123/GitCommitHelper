LANGUAGES = {
    "ko": {
        "select_commit": "커밋 메시지 선택:",
        "title_input": "제목 입력란",
        "description_input": "설명문 입력란",
        "copy": "복사하기"
    },
    "en": {
        "select_commit": "Select commit text:",
        "title_input": "Title input",
        "description_input": "Description input",
        "copy": "Copy"
    }
}

def get_text(key, lang="ko"):
    return LANGUAGES.get(lang, LANGUAGES["ko"]).get(key, key)
