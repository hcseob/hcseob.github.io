# How to use this repo
1. Create a file 'init.sh' with contents:
> #!/bin/sh <br>
> source venv/bin/activate <br>
> export OPENAI_API_KEY='sk-...'

2. Create a virtual env: `python -m venv venv`
3. Install `requirements.py`
4. Execute `source init.sh`
5. Reset the pages `python python/reset.py`
6. Create pages (e.g. 100 in this example) `python python/run.py 100`

