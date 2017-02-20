# File System Overview

This document describes how the file system of the repo is organized.

```
tree -R -L 5 -d
source
├── Team_Documentation                      -- contains all Team Documentation
│   ├── Team_1
│   ├── Team_2
│   └── Team_3
│       ├── Meeting_Minutes
│       ├── presentations
│       ├── project_documents
│       └── weekly_reports
├── database                                -- contains the database file
├── deploy_tools                            -- various scripts for deploying to a server
└── group1
    ├── comm
    │   ├── migrations                      -- database migration scripts for the chat app
    │   ├── static                          -- assets for the HTML template pages
    │   │   ├── emoji
    │   │   └── uploads
    │   └── templates                       -- HTML templates for the chat app
    │       └── comm
    ├── communication
    │   ├── django
    │   │   ├── comm
    │   │   │   ├── migrations
    │   │   │   └── templates
    │   │   └── group2
    │   ├── node                            -- root directory for the node-based chat app
    │   │   ├── node_modules                -- node dependencies
    │   │   └── test                        -- javascript unit tests for chat app
    │   └── tests                           -- python unit tests for django app
    ├── functional_tests                    -- python integration tests
    ├── group1                              -- chat tool MVC code
    ├── issue_tracker                       -- issue tracker MVC code
    │   ├── management
    │   │   └── commands
    │   ├── migrations                      -- database migrations scripts for issue tracker
    │   ├── static                          -- assets for the HTML template pages
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── images
    │   │   ├── js
    │   │   └── libs
    │   ├── templates                       -- HTML templates for issue tracker
    │   └── tests                           -- unit tests for issue tracker
    ├── project_router                      -- project router MVC code
    │   ├── migrations
    │   ├── static
    │   ├── templates
    │   └── tests
    └── requirements                        -- requirements MVC code
        ├── migrations
        ├── models
        ├── static
        ├── templates
        ├── templatetags
        ├── tests
        └── views

92 directories
```