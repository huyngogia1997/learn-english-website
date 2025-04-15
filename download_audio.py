import os
import json
import requests

# Tạo thư mục audio nếu chưa tồn tại
os.makedirs("audio", exist_ok=True)

# Đọc cấu trúc JSON từ file
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Hàm tải âm thanh
def download_audio(url, filename):
    try:
        print(f"Đang tải: {filename}")
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra nếu HTTP request không thành công
        with open(f"audio/{filename}", "wb") as f:
            f.write(response.content)
        print(f"Tải hoàn tất: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi khi tải {filename}: {e}")

# Tải từng âm thanh từ JSON
for question in questions:
    audio_url = question["audio"]
    filename = audio_url.split("/")[-1]  # Lấy tên tệp từ URL
    download_audio(audio_url, filename)

print("Tải tất cả âm thanh xong!")
