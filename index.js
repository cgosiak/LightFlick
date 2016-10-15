var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {

    var lightIsOn = false;

    var spawn = require('child_process').spawn,
	py = spawn('python3', ['./off.py']),
	dataString = '';

    socket.on('shake', function() {
            // Shake has taken place
            console.log("Shook!");

            if (lightIsOn) {
                var spawn = require('child_process').spawn,
                    py = spawn('python3', ['./off.py']),
                    dataString = '';
            } else {
                var spawn = require('child_process').spawn,
                    py = spawn('python3', ['./on.py']),
                    dataString = '';
            }

            py.stdout.on('data', function(data) {
                dataString += data.toString();
                console.log(dataString);
            });

            lightIsOn = !lightIsOn;
    });

});

http.listen(4545, function() {
    console.log('listening on *:4545');
});
