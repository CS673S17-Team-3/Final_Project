SELENIUM_README.md

## create demo-data
```
python manage.py populate_demo_data
```

install firefox browser

http://stackoverflow.com/questions/6682009/selenium-firefoxprofile-exception-cant-load-the-profile
pip install -U selenium

http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
download geckodriver from here: https://github.com/mozilla/geckodriver/releases
    unzip tar.gz
    move geckodriver binary to ~/g1
    add path/to/geckodriver/binary to $PATH (export PATH=$PATH:~/g1/)



make sure both web-app and nodejs are running

activate virtualenv
export PATH=$PATH:~/g1/

python manage.py test
or
python manage.py test /path/to/test
