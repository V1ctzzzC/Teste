from flask import Flask
from google.cloud import storage
import json

app = Flask(__name__)

BUCKET_NAME = "testevh"
FILE_NAME = "olá.json"

def read_json_from_gcs():
    """Lê o arquivo JSON do bucket do Google Cloud Storage."""
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        json_data = blob.download_as_text()
        return json.loads(json_data)
    except Exception as e:
        return {"error": f"Erro ao ler o arquivo JSON: {e}"}

@app.route('/')
def hello():
    """Retorna o conteúdo do arquivo JSON na tela."""
    data = read_json_from_gcs()
    return f"<pre>{json.dumps(data, indent=2, ensure_ascii=False)}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.1', port=8080, debug=True)
