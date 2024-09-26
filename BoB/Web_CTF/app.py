from flask import Flask, request, send_from_directory, after_this_request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import os
import hashlib
import base64
import threading
import time


FLAG = "flag{onestar_fake}"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(__file__) + "/tmp/"



def delayed_file_removal(file_path, delay):
    time.sleep(delay)
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")

@app.route('/111111/')
def htmltopdf():
    return 'Flag is here -> /111111/flag<br><br>Try this! -> <a href="/111111/generate-pdf?html=<h1>test</h1>">gogo</a>'

@app.route('/111111/generate-pdf')
def generate_pdf():
    html_content = "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none';\">\n"
    html_content += request.args.get('html')

    if not html_content:
        return 'No HTML content provided', 400
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(10)


    tmp_file = app.config['UPLOAD_FOLDER'] + hashlib.sha256(os.urandom(64)).hexdigest()


    with open(tmp_file + ".html", 'w') as file:
        file.write(html_content)

    driver.get('file://' + tmp_file + ".html")

    try:
        driver.switch_to.alert.accept()
    except:
        pass


    pdf_data = driver.execute_cdp_cmd('Page.printToPDF', {
        'format': 'A4'
    })

    driver.close()
    driver.quit()
    
    with open(tmp_file + ".pdf", 'wb') as pdf_file:
        pdf_file.write(base64.b64decode(pdf_data['data'].encode()))
    
    @after_this_request
    def remove_files(response):
        threading.Thread(target=delayed_file_removal, args=(tmp_file + ".html", 5)).start()
        threading.Thread(target=delayed_file_removal, args=(tmp_file + ".pdf", 5)).start()

        return response


    return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(tmp_file + ".pdf"))


@app.route('/111111/flag')
def flag():
    if request.remote_addr == "127.0.0.1":
        return FLAG
    else:
        return "Only access local!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')