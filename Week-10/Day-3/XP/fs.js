let fs = require('fs');


const promisToReadFile = async filePath => fs.promises.readFile(filePath, 'utf-8')

const promisToWriteToFile = async (filePath, data, ...options) => 
                            fs.promises.writeFile(filePath, data+'\n', ...options)
    // options: It is an string or object that can be used to specify optional parameters that will 
    // affect the output. It has three optional parameter:
    //  - encoding: It is a string value that specifies the encoding of the file. The default value is ‘utf8’.
    //  - mode: It is an integer value that specifies the file mode. The default value is 0o666.
    //  - flag: It is a string value that specifies the flag used while writing to the file. The default value is ‘w’.        

//read original file
promisToReadFile('test.txt').then((data) => {
    console.log(data)
}) .catch ((err) => {
    console.log('We are experiencing a problem with reading file. The error message is: ',err)
})


//lets create new file and write there  content of the new Content
// we use  flag 'w' 
let newContent = 'new content'

promisToWriteToFile('test1.txt',newContent,{'encoding': 'utf8', 'flag':'w'})
.then((data1) => {
    promisToReadFile('test1.txt')
    .then((data2) => {
        console.log(data1)
        promisToWriteToFile('test1.txt', appendedContent, {'encoding': 'utf8', 'flag':'a'})
        .then((data) => {
            console.log('File has been changed successefully')
            promisToReadFile('test1.txt')

        })
        
        


    console.log('File has been changed successefully')
}) 
.catch ((err) => {
    console.log('We are experiencing a problem with files system. The error message is: ',err)
})


//should recived newly created file with new content
promisToReadFile('test1.txt').then((data) => {
    console.log(data)
}) .catch ((err) => {
    console.log('We are experiencing a problem with reading file. The error message is: ',err)
})


//lets append somethign to the file
//user flag 'a'

let appendedContent = 'Appened content'

promisToWriteToFile('test1.txt', appendedContent, {'encoding': 'utf8', 'flag':'a'})
.then((data) => {
    console.log('File has been changed successefully')
}) 
.catch ((err) => {
    console.log('We are experiencing a problem with files system. The error message is: ',err)
})

//should recived two lines of code now file with new content
promisToReadFile('test1.txt').then((data) => {
    console.log(data)
}) .catch ((err) => {
    console.log('We are experiencing a problem with reading file. The error message is: ',err)
})

