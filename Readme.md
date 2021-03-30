## Simplar project
This is the backend for the Simplar project.
The backend is already running on a server hosted in Google Cloud.

## How to run
### Requirements
Ubuntu 18.04  
Python 3.6  
(Enough RAM)  
(GPT-3 API Key)

### (install build essentials on linux)
sudo apt-get update  
sudo apt-get install build-essential

### change locale
export LANG="en_US.UTF-8"

### Download project
https://github.com/sutedalm/simplar-server.git  
cd simplar-server

### create virtual environment

python3 -m venv venv  
source venv/bin/activate

### update pip

python -m pip install --upgrade pip

### install requirements

pip --no-cache-dir install -r requirements.txt

### download nltk

python3
import nltk
nltk.download('all-nltk')

### To start debug server
python3 wsgi.py

### To run server
gunicorn -b :8080 wsgi:app
