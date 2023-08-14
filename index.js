var express = require("express");
var cors = require("cors");
var path = require("path");

var app = express();

app.use(express.static(path.join(__dirname, 'client')));


app.use(cors());
app.use(express.json());

app.listen(3000, () => {
    console.log("Server running on port 3000");
});

app.get("/url", (req, res, next) => {
    res.json(["Tony","Lisa","Michael","Ginger","Food"]);
});

app.post("/test", (request, response) => {
    console.log(request.body);
    response.send({
        message: request.body
    });
});