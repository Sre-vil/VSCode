// const express = require('express')
// const app = express()

// app.get('/', function (req, res) {
//   res.send('Hello World')
// })

// app.listen(3000)

const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/dog', (req, res) => {
    res.send({'sound': '멍멍'}) // javascript object 자료형임
})

app.get('/cat', (req, res) => {
    res.json({'sound': '야옹'}) // json 자료형임
})

// 변수를 받는 방법
app.get('/user/:id', (req, res) => {
    const q = req.params
    console.log(q)
    console.log(q.id)
    res.json({'userid': q.id})

    const q2 = req.query
    console.log(q2)
    console.log(q2.q)
    console.log(q2.name)
    res.json({'userid': q2.name})
})

//post 방식
app.post('/user/:id', (req, res) => {
    const p = req.params
    console.log(p)
    const b = req.body
    console.log(b)

    res.send({'message' : 'post success'})
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
