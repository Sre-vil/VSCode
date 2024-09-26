const express = require('express')
var cors = require('cors')
const app = express()
const port = 3000 

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.use(cors()) // () 비워두면 모든 요청을 허용. 조건 설정 가능함 

// {}안에 KEY 값을 입력하여 사용하면 더욱 간단함 
app.get('/sound/:name', (req, res) => {
    const { name } = req.params
    console.log(name) // 여기 적힌 name 값에 url 로 전달한 :name parameter 값이 들어감

    if(name == "dog"){
        res.json({'sound': '멍멍'})
    } else if(name=="cat")
    {
        res.json({'sound': '야옹'})
    } else if (name == "pig")
    {
        res.json({'sound': '꿀꿀'})
    } else {
        res.json({'sound': '알 수 없음'})
    }
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})