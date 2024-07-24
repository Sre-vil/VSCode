import base64
import zipfile

encoded_str = "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"

decoded_bytes = base64.b64decode(encoded_str)
with open('decoded.zip', 'wb') as file:
    file.write(decoded_bytes)

with zipfile.ZipFile('decoded.zip', 'r') as zip_ref:
    zip_ref.extractall('pdf_output')
