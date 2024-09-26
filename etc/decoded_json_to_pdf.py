import json
import base64

def decode_base64_content(encoded_content, output_path):
    """ Base64로 인코딩된 내용을 디코딩하여 파일로 저장하는 함수 """
    # Base64 디코딩
    decoded_content = base64.b64decode(encoded_content)
    # 디코딩된 내용을 파일로 저장
    with open(output_path, 'wb') as file:
        file.write(decoded_content)
    print(f"File saved to {output_path}")

def process_json_file(file_path, output_path):
    """ JSON 파일을 처리하는 함수 """
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 파일명 디코딩 (유니코드 파일명 처리)
    readable_title = json_data['title']

    # Base64 내용 디코딩 및 파일로 저장
    decode_base64_content(jsobn_data['content'], output_path + readable_title)

    # 결과 출력
    print(f"Decoded Title: {readable_title}")

    return readable_title

# 함수 호출 예시
file_path = 'test2.json'  # JSON 파일의 경로
output_path = '.'  # 디코딩된 파일을 저장할 경로
decoded_title = process_json_file(file_path, output_path)