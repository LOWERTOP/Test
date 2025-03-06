import os
import requests

# 从环境变量中获取 API KEY，请确保这个文件保存为 .py 文件
DEEPOSEEK_API_KEY = sk-bf3326665ba740839aa923d5f6483e33("DEEPOSEEK_API_KEY")
DEEPOSEEK_API_URL = "https://api.deepseek.com/v1"  # 根据实际文档调整 URL

def translate_text(text, source_lang="auto", target_lang="en"):
    headers = {
        "Authorization": f"Bearer {DEEPOSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "source_language": source_lang,
        "target_language": target_lang
    }
    response = requests.post(DEEPOSEEK_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result.get("translated_text", "")
    else:
        print("Translation error:", response.text)
        return None

def main():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print("读取 README.md 失败:", e)
        return

    translated = translate_text(content)
    if translated:
        with open("README.EN.MD", "w", encoding="utf-8") as f:
            f.write(translated)
        print("Translation successful, README.EN.MD updated.")
    else:
        print("Translation failed.")

if __name__ == "__main__":
    main()
