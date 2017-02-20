# Testing
This document describes how to run the Django test suite for **python** code.

## Prerequisites
* The application is installed and configured according to the (README.md) README document.
* The virtualenv is active during the test run.

## Running tests
To run the entire Django test suite, execute this command in a terminal session with an active virtualenv:
```bash
python manage.py test
```

You should see output in your terminal session that looks like so:
```bash
Creating test database for alias 'default'...
................................................EEEEEEEEEEEEEE
======================================================================
```

The 'periods' indicate a test that has passed.
The 'E' indicates a test that has failed.

If a test has failed, you should see output that looks similiar to:
```bash
======================================================================
ERROR: test_user_project_and_iteration_permission (requirements.tests.ui.test_user_project_and_iteration_permission.TestUserProjectAndIterationPermission)
----------------------------------------------------------------------
Traceback (most recent call last):
... (STACKTRACE HERE)
...
```

The output describes how the test failed, along with the stacktrace (called 'Traceback') showing how it failed.

It will be your responsibility for running the test suite and fixing all broken tests before check-in, as well as when the branch is merged into the development branch.

## Location of Test suites
Tests should be written near the feature they are testing. Currently, we have test suites in the following locations:
* group1/communication/tests
* group1/functional_tests
* issue_tracker/tests
* project_router/tests
* requirements/tests

## Writing Tests
In order to write a test for a feature, locate the test suite the represents the "area of concern". For instance, if you are working on the communication tool, you would look for the test suite in **group1/communication/tests**.

Once you have located the test suite, survey the test file to get a sense for how the tests are organized. Generally, tests within a test suite will be organized within "test classes" that are concerned with a specific area of the code. For instance, in **group1/communication/tests/tests.py**, we see at least 4 (four) different Test Classes:
* TestInfrastructure -- tests for basic infrastructure
* TestAPI            -- tests for API's to the Django app
* TestSocketIO       -- tests for the API's to the SocketIO-based Chat tool
* SeleniumTests      -- browser-based tests, using the Selenium WebDriver

If you are writing a test for a new, or existing API within the Django app, then you would add the test to the TestAPI class.

If you find that none of the Test Classes really describe the code you are trying to test, create a new Test Class following the conventions that already exist within the test file.

For more reference on Django testing, please see this documentation: https://docs.djangoproject.com/en/1.10/topics/testing/overview/

