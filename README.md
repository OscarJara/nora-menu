# Nora's menu

This repository contains the source code for the nora menu made in python 3.7.

# Installation

* you will need to install the python packages located in the requirements.txt

```bash
 pip install -r requirements.txt
```

* Once the project packages are installed, you must execute the following commands, in order to raise the models.

```python
python manage.py makemigrations
python manage.py migrate
```

* If you don't have a redis server, you should create a local one and run it, to be able to run the project, since celery needs one to be able to run as expected.
* If you have a server, you should add the ip in the following path: `applications.library.celery.celery_.py`, in` BROKER_URL`

```bash
brew update
brew install redis
```

* then you must execute celery, from the local configuration found in the `applications.library.celery.celery_.py` directory with the following command.

```bash
celery worker -A applications.library.celery.celery_ --loglevel = info
```

* `--loglevel = info` is used to obtain real-time information regarding the tasks added to celery.

* The last missing file is the `.env` a secret configuration file, the file must be created in the path: `applications.library` and inside it add the following variable:

```bash
BOT_SLACK_TOKEN = 'xoxb-1357458481509-1357460507253-XCaxZW5SNoWo6JmfdZrU2s1F'
```

this is the authentication token for the Slack integration.

* Having all this done, the tests should be executed, to verify that everything is perfectly configured:

```python
python manage.py test
```

Where the expected response is the following:

```python
Creating test database for alias 'default' ...
System check identified no issues (0 silenced).
...............................
-------------------------------------------------- --------------------
Ran 33 tests in 1.716s

okay
Destroying test database for alias 'default' ...
```

* now that it is verified that the installation and configuration does not present problems, it should be raised with the following command:

```python
python manage.py runserver
```

# Example of integration with slack

! [Message in slack]
(https://github.com/OscarJara/nora-menu/blob/master/message_in_slack.png)