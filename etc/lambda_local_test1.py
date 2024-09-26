import json
from PyPDF2 import PdfReader

def process_pdf_to_json(pdf_file_path, json_file_path):
    try:
        # PDF 파일 읽기
        with open(pdf_file_path, "rb") as file:
            reader = PdfReader(file)
            all_text = ''
            for page in reader.pages:
                all_text += page.extract_text() or ''  # Safely handle pages where text extraction returns None
            
            # Create data in JSON format
            data = {
                "title": pdf_file_path,
                "content": all_text
            }
            json_data = json.dumps(data, ensure_ascii=False)  # Convert Python dictionary to JSON string

            # JSON 데이터를 파일로 저장
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            print(f"File processed and stored as JSON in {json_file_path}")
    
    except Exception as e:
        print(e)
        print(f'Error processing the file {pdf_file_path}.')
        raise e

# 파일 경로는 여기서 직접 설정
pdf_file_path = '킥오프_대본.pdf'  # PDF 파일 경로
json_file_path = 'kick.json'  # JSON 파일로 저장할 경로 

# 함수 호출
process_pdf_to_json(pdf_file_path, json_file_path)