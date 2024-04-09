const fs = require("fs")

fs.readFile("number_one.txt", 'utf8', (err, data) => {
    if(err){
        console.log('파일을 읽는 도중 오류가 발생했습니다.', err)
        return;
    }

    console.log("파일 내용 : ", data)
})
let content = "Sa Sa Sa"
fs.writeFile("number_four.txt", content, (err) => {
    if(err){
        console.log("파일을 쓰는 도중 오류가 발생했습니다.", err)
        return;
    }
    console.log("파일 내용: ", content)
})

let text = "Hello"
fs.appendFile("newfile.txt", text, (err) => {
    if(err){
        console.log("파일을 쓰는 도중 오류가 발생했습니다.", err)
        return;
    }
    console.log("파일 내용: ", text)
})