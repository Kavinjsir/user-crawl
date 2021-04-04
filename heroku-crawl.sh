#!/bin/bash
#export AWS_ACCESS_KEY_ID=
#export AWS_SECRET_ACCESS_KEY=
#export AWS_DEFAULT_REGION=
#export MONGO_URL=''
#export DOWNLOAD_FILENAME=''
echo "MONGO_URL = '$MONGO_URL'" >> settings.py
python run_spider.py user
