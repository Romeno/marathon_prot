@echo off
pushd I:\Romeno\Projects\PyCharm\marathon
python ./manage.py compilemessages -v 3
popd
PAUSE