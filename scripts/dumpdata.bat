@echo off
pushd I:\Romeno\Projects\PyCharm\marathon
python ./manage.py dumpdata auth.user --indent 4 --output fixtures\initial_data.json
python ./manage.py dumpdata marathon_marathons --indent 4 --output marathon_marathons\fixtures\initial_data.json

python ./manage.py dumpdata marathon_common --indent 4 --output marathon_common\fixtures\initial_data.json
python ./manage.py dumpdata marathon_expo --indent 4 --output marathon_expo\fixtures\initial_data.json
popd
PAUSE