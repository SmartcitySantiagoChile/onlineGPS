## TO RUN TESTS

To run tests of this app you need to run members as follow:

````bash
coverage run --source='.' manage.py test timeperstreet --settings=timeperstreet.tests.settings
```

The option `--settings` let you give a different setting file. We use to change the migrations folder of app to create legacy tables 
