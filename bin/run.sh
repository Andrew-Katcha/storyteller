# !/bin/bash

export FLASK_DEBUG=True
export FLASK_APP=storyteller
export STORYTELLER_SETTINGS=config.py

flask run --host 0.0.0.0 --port 8000
