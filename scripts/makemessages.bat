@echo off
pushd I:\Romeno\Projects\PyCharm\marathon
python ./manage.py makemessages -l ru -v 3 --keep-pot --no-wrap --no-location -i "tinymce" -i "locale" -i "*.bat" -i "*.png" -i "*.md" -i "requirements.txt"
popd
PAUSE