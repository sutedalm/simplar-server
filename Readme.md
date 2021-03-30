## Simplar project
This is the backend for the Simplar project.
The backend is already running on a server hosted in Google Cloud.

## How to run
### Requirements
Ubuntu 18.04  
Python 3.6  
(Enough RAM)  
(GPT-3 API Key)

### (Install build essentials on linux):
```
sudo apt-get update  
sudo apt-get install build-essential
```

### Change locale:
```
export LANG="en_US.UTF-8"
```

### Download project:
```
git clone https://github.com/sutedalm/simplar-server.git  
cd simplar-server
```

### Create virtual environment:
```
python3 -m venv venv  
source venv/bin/activate
```

### Update pip:
```
python -m pip install --upgrade pip
```

### Install requirements:
```
pip --no-cache-dir install -r requirements.txt
```

### Download nltk:
```
python3
import nltk
nltk.download('all-nltk')
```

### To start debug server:
```
python3 wsgi.py
```

### To run server:
```
gunicorn -b :8080 wsgi:app
```
The JSON request should look like this:
```
{
  "data": [
    "Owls hunt mostly small mammals, insects, and other birds though some species specialize in hunting fish."
  ],
    "useGPT3": false,
    "enableSummarizer": false
}
```
"data": List of strings(sentences), each of them is simplified separately.
"useGPT3": Boolean, enables GPT3 if true. However, you need to have an acces key.
Save the access key as an environement variable with:
```
export GPT3_KEY:"your_key"
```
"enableSummarizer": enables summarizer. Summarized Text is then simplified.

### Credits:
https://github.com/facebookresearch/access.git

