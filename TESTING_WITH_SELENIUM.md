SELENIUM_README.md

In order to run the Selenium tests, you will need to create some "demo" data to populate your DB.

Create the demo data like so:

```
python manage.py populate_demo_data
```

The Selenium Webdriver is based off the Firefox binary. As a result, you will need to install the Firefox browser.

Install the selenium python dependency into your virtualenv:
```
pip install -U selenium
```

Install the geckodriver:
```
https://github.com/mozilla/geckodriver/releases
```

Unzip the geckodriver, and copy it to the root level directory "g1".

Update your $PATH with the geckodriver location:
```
export PATH=$PATH:~/g1
```

Make sure both web-app and nodejs are running in separate terminal sessions.
Make sure your third terminal session has an 'activated' virtualenv.

To run the tests:
```
python manage.py test
or
python manage.py test /path/to/test
```