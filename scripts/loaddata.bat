@echo off
pushd I:\Romeno\Projects\PyCharm\marathon
python ./manage.py loaddata initial_data.json
popd
PAUSE