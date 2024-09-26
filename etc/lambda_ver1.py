import json
import urllib.parse
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        response = s3.get_object(Bucket=source_bucket, Key=key)
        file_content = base64.b64encode(response['Body'].read()).decode('utf-8')  # 바이너리 파일 내용을 Base64 인코딩
        
        # JSON 형태로 데이터 생성
        data = {
            "title": key,
            "content": file_content
        }
        json_data = json.dumps(data, ensure_ascii=False)  # Python dictionary를 JSON 문자열로 변환

        # JSON 데이터를 S3 버킷에 저장
        s3.put_object(Bucket='bob13-jsonstorage', Key=key + '.json', Body=json_data, ContentType='application/json')
        print("File processed and stored as JSON in 'bob13-jsonstorage'")
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, source_bucket))
        raise e