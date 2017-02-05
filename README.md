# Final Project, MET CS 673

Last modified Spring 2017.

These instructions may be followed on any Unix-like system, including OS X.

## Getting started

First, clone this repos and checkout the `develop` branch:

```
$ git clone https://github.com/CS673S17-Team-2/Final_Project.git
$ cd Final_Project
$ git checkout develop
```

Create a Python virtualenv in a `venv` directory and activate it:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install the Python requirements using `pip`:

```
$ pip install -r requirements.txt
```

Create the database:

```
$ mkdir database
$ python manage.py makemigrations
$ python manage.py migrate
```

Create an admin user for use with Django and the project management
applications, e.g. username: `admin`, password `admin`.

```
$ python manage.py createsuperuser
```

Now start the server:

```
$ python manage.py runserver
```

You should see a message telling you the server is running at
`http://127.0.0.1:8000/`. Open this URL in a browser. This is the Django backend
for the project management application. It handles both the browser-based
interface and the RESTful RPC backend used by the chat application.

If you'd like to use the chat application, you'll need to create a default chat
channel and start the Node service to handle passing websocket messages between
the browser interface and the Django backend. 

To create a channel without starting the web interface, use `curl`:

```
$ curl -H "Content-Type: application/json" -X POST -d '{"name":"Test","description":"Test team","public":true}' http://localhost:8000/api/rooms/
```

Prepare the Node server by making sure all your node modules are up-to-date:

```
$ cd Final_Project/group1/communication/node
$ npm install
```

Then you can start the Node server:

```
$ node main.js
```

You should now be able to open the [chat application on your location
server](http://127.0.0.1:8000/communication/) in your browser and log in to use
chat.


# Previous documentation

### SERVER INSTALLATION (*nix systems)
###### note: follow the commands under deploy_tools serverInstallcommands.sh (not tested as an executable shell script)
###### note: must have fabric installed (on windows this will require a manual installation (setup_py) of pycrypto first, you may find pre-compiled windows binaries here (http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
##### change directory to where deploy_tools is on your local computer - this script is deployed from your local computer to the server
cd /c/g1/source/deploy_tools
###### note: must activate virtualenv with fabric (you may have fabric installed on your path python, and not require a virtualenv)
##### run the fabfile.py script with the following command to upload the project from origin/master to the specified server
fab deploy:host=pgmvt@dev.3blueprints.com
