import time

# (이전 코드와 동일한 부분)

for id in range(start_id, end_id + 1):
    url = f"{base_url}{id}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Request successful for ID {id}")
            print(f"Response for ID {id}: {response.text}")
        else:
            print(f"Request failed for ID {id} with status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error with ID {id}: {e}")
    
    time.sleep(0.5)  # 0.5초 대기