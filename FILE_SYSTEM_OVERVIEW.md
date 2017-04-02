# File System Overview

This document describes how the file system of the repo is organized.

```
tree -R -L 5 -d
source
├── Team_Documentation
│   ├── Team_1
│   ├── Team_2
│   └── Team_3
│       ├── Meeting_Minutes
│       ├── presentations
│       ├── project_documents
│       └── weekly_reports
├── database
├── deploy_tools
└── group1
    ├── comm
    │   ├── migrations
    │   ├── static
    │   │   ├── emoji
    │   │   └── uploads
    │   ├── templates
    │   │   └── comm
    │   └── tests
    ├── communication
    │   ├── django
    │   │   ├── comm
    │   │   │   ├── migrations
    │   │   │   └── templates
    │   │   └── group2
    │   ├── node
    │   │   ├── node_modules
    │   │   │   ├── basic-auth
    │   │   │   ├── debug
    │   │   │   ├── depd
    │   │   │   ├── ee-first
    │   │   │   ├── express
    │   │   │   ├── express-cors
    │   │   │   ├── lodash
    │   │   │   ├── mocha
    │   │   │   ├── morgan
    │   │   │   ├── ms
    │   │   │   ├── multer
    │   │   │   ├── node-rest-client
    │   │   │   ├── on-finished
    │   │   │   ├── on-headers
    │   │   │   ├── request
    │   │   │   ├── restler
    │   │   │   ├── socket.io
    │   │   │   ├── supertest
    │   │   │   └── unit.js
    │   │   └── test
    │   └── tests
    ├── group1
    ├── issue_tracker
    │   ├── management
    │   │   └── commands
    │   ├── migrations
    │   ├── static
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── images
    │   │   ├── js
    │   │   └── libs
    │   └── templates
    ├── project_router
    │   ├── migrations
    │   ├── static
    │   └── templates
    ├── requirements
    │   ├── migrations
    │   ├── models
    │   ├── static
    │   │   ├── bootstrap
    │   │   │   ├── css
    │   │   │   ├── fonts
    │   │   │   └── js
    │   │   ├── bs-datetimepicker
    │   │   │   ├── css
    │   │   │   ├── js
    │   │   │   └── less
    │   │   ├── css
    │   │   ├── images
    │   │   ├── img
    │   │   ├── js
    │   │   ├── projects
    │   │   └── sb-admin
    │   │       ├── css
    │   │       └── font-awesome
    │   ├── templates
    │   ├── templatetags
    │   ├── tests
    │   └── views
    └── selenium_tests
        ├── issue_tracker
        ├── project_router
        └── requirements

92 directories
```