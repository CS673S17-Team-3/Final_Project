SELENIUM_README.md

In order to run the Selenium tests, you will need to execute the following steps:


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


To run all of the Selenium tests:
```
python manage.py test --liveserver=127.0.0.1:8000 selenium_tests
```

To run the Project Router App Selenium tests:
```
python manage.py test --liveserver=127.0.0.1:8000 selenium_tests.project_router
```

To run the Requirements App Selenium tests:
```
python manage.py test --liveserver=127.0.0.1:8000 selenium_tests.requirements
```

To run the Issue Tracker App Selenium tests:
```
python manage.py test --liveserver=127.0.0.1:8000 selenium_tests.issue_tracker
```