// Express and SocketIO boilerplate
var app = require('express')();
var morgan = require('morgan')
var http = require('http').Server(app);
var io = require('socket.io')(http);
var Client = require('node-rest-client').Client;
var os = require('os');
var util = require('util');
var _ = require('lodash');
var multer = require('multer');
var fs = require('fs');
var crypto = require('crypto');

app.use(morgan('combined'))

// Add CORS headers to all express requests
app.all('/*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    next();
});

// just for file upload
var done = false;
app.use(multer({
        'dest': '../../../../static/uploads',
        onFileUploadStart: function(file) {
                console.log(file.originalname + ' is starting...');
        },
        onFileUploadComplete: function(file) {
                console.log(file.fieldname + ' uploaded to ' + file.path);
                done = true;
        }
}));

app.post('/upload', function(req,res){
        if (done==true) {
                var hash = crypto.randomBytes(20).toString('hex');
                fs.mkdir( util.format('/home/pgmvt/sites/www.3blueprints.com/static/uploads/%s', hash), function(){
                        var final_path = util.format('%s/%s', hash, req.files.fileUpload.originalname);
                        fs.rename(req.files.fileUpload.path, '/home/pgmvt/sites/www.3blueprints.com/static/uploads/' + final_path);
                        res.send('static/uploads/' + final_path);
                });
        }
});

var client = new Client();

// We should stash the username (ID?) of everyone connected to the global namespace here
var users = [];

var global_namespace = io.of('/');
global_namespace.on('connection', function(socket){
        var user;
        socket.on('user', function(msg) { 
                console.log(msg);
                user = msg.username;
                users.push(user);
                global_namespace.emit('user', {'username': user, 'action': 'connected' });
                console.log( util.format('%s connected', user) );
        });
        socket.on('disconnect', function(){
                users.pop(user);
                console.log( util.format('%s disconnected', user) );
                global_namespace.emit('user', {'username': user, 'action': 'disconnected' });
        });
        socket.on('room', function(room){
                console.log('new room: '  + room.name);
                rooms.save(room.name, room.creator_id, room.description, room.public);
        });
        socket.on('updateroom', function(room){
                rooms.update(room);
                global_namespace.emit('updateroom', room);
        });
        socket.on('deleteroom', function(room) {
                rooms.delete(room);
                global_namespace.emit('deleteroom', room);
        });
});


// Make a REST call to get the currently connected users

app.get('/users', function(req,res){
        res.header
        res.send(_.unique(users));
});

var room_url = 'http://localhost:8000/api/rooms/?format=json';

namespaces = {}

function add_new_namespace(room) {
  namespaces[room.id] = io.of(util.format('/%s', room.id))
    .on('connection', function(socket) {
        console.log(util.format('conncted to room %s', room.id ));
       socket.on('msg',function(msg){
           console.log(util.format('message from %s: %s', msg.username, msg.value));
         namespaces[room.id].emit('msg', msg);
         messages.save(room.id, util.format('%s: %s', msg.username, msg.value), msg.user_id);
       });
       socket.on('disconnect',function(){
         console.log(util.format('someone disconnected from %s', room.id ));
       });
  });
}

client.get(room_url,function(data,response){
  data.forEach(function(room){
    add_new_namespace(room);
  });
});

var messages = {
        'save': function(room_id, message, user_id) {
                message_template = {
                        data: {
                                'at_message': false,
                                'room': util.format('http://localhost:8000/api/rooms/%s/', room_id),
                                'user': util.format('http://localhost:8000/api/users/%s/', user_id),
                                'text': message 
                        },
                        headers: { 'Content-Type': 'application/json' }
                };
                client.post('http://localhost:8000/api/messages/', message_template, function(data,response) {
                        console.log( util.format('(%s) Room %s : "%s"', response.statusCode, room_id, message) );
                });
        }
}

var rooms = {
        'save': function(name, creator_id, desc, pub) {
                room_template = {
                        data: {
                                'name': name,
                                'creator': util.format('http://localhost:8000/api/users/%s/', creator_id),
                                'description': desc,
                                'public': pub,
                        },
                        headers: { 'Content-Type': 'application/json' }
                };
                client.post('http://localhost:8000/api/rooms/', room_template, function(data,response) {
                        console.log( util.format('(%s) Room %s created by user "%s"', response.statusCode, name, creator_id) );
                        add_new_namespace(data);
                        global_namespace.emit('room', data);
                });
        },
        'update': function(room) {
                room_template = {
                        data: {
                                'id': room.id,
                                'name': room.name,
                                'creator': room.creator,
                                'description': room.description,
                                'public': room.public,
                        },
                        headers: { 'Content-Type': 'application/json' }
                };
                client.put('http://localhost:8000/api/rooms/', room_template, function(data,response) {
                        console.log( util.format('(%s) Room %s updated to "%s"', response.statusCode, room.id, room.name) );
                });
        },
        'delete': function(room) {
                room_template = {
                        data: {
                                'id': room.id,
                        },
                        headers: { 'Content-Type': 'application/json' }
                };
                client.delete('http://localhost:8000/api/rooms/', room_template, function(data,response) {
                        console.log( util.format('(%s) Room %s was deleted', response.statusCode, room.id) );
                });
        }
}


var msg_endpoint = 'http://127.0.0.1:8000/api/messages/'

var message_template = {
        "data": {
                "at_message": false,
                "room": "http://localhost:8000/api/rooms/1/",
        "user": "http://localhost:8000/api/users/1/"
        },
        "headers": { "Content-Type": "application/json" }
}

// WebSocket stuff
io.on('connection', function(socket) {
        socket.on('msg', function(msg) {
                io.emit('msg', msg);
                message_template.data.text = msg;
                client.post(msg_endpoint, message_template, function(data,response) { console.log(msg) });
        });
});

// Start the server
http.listen(3000, function(){
        console.log('Starting NodeJS server');
        console.log('listening on 3000');
});
