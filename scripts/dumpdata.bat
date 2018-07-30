@echo off
pushd I:\Romeno\Projects\PyCharm\marathon
python ./manage.py dumpdata marathon_common --indent 4 --output marathon_common\fixtures\initial_data1.json
python ./manage.py dumpdata marathon_runner --indent 4 --output marathon_runner\fixtures\initial_data1.json
popd
PAUSE