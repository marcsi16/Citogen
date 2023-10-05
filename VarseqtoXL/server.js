var http = require("http");
var fs = require("fs");

http.createServer(function (request, response) {
   // Check if the request URL is the root ("/")
   if (request.url === '/') {
      // Send the HTTP header
      // HTTP Status: 200 OK
      // Content Type: text/html
      response.writeHead(200, {'Content-Type': 'text/html'});

      // Read the HTML file and send it as the response body
      fs.readFile('index.html', function(err, data) {
         if (err) {
            // Handle any error, e.g., file not found
            response.writeHead(404);
            response.end("404 Not Found");
         } else {
            // Send the HTML content as the response body
            response.end(data);
         }
      });
   } else {
      // For any other URL, respond with a 404 error
      response.writeHead(404);
      response.end("404 Not Found");
   }
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
