const express = require('express');
const app = express();
const ip = require('ip');
const axios = require('axios');
const url = require('url');


const port = 3000
const FLAG = "BoB{fake_onestar_flag}"


app.get('/111111/', (req, res) => {
  res.send('<a href="/111111/request?input=http://127.0.0.1:3000/111111/flag">go</a>')
})

app.get('/111111/request', (req, res) => {
    const input = req.query.input;
    var urlObj = url.parse(input);
    console.log(urlObj);

    var hostname = urlObj.hostname;

    if(ip.isPrivate(hostname)){
        res.send("No Hack!!!");
    }else{
        axios.get(input)
        .then(response => {
            res.send(response.data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    
})

app.get('/111111/flag', (req, res) => {

    var remote_ip = req.headers['X-Real-IP'] || req.connection.remoteAddress;

    if (remote_ip.substr(0, 7) == "::ffff:") {
        remote_ip = remote_ip.substr(7)
    }


    if(remote_ip==='127.0.0.1'){
        res.send(FLAG);
    }else{
        res.send("Only access private network!!!")
    }
  })

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})