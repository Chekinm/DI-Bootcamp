class Video {
    constructor (title, uploader, time){
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    } 
    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`)
    }
}

firstVideo = new Video('Kill Bill', 'Mike', 345)
secondVideo = new Video('Star Wars', 'John', 456)

firstVideo.watch()
secondVideo.watch()
console.log(Video.toString())


video_catalog = [
    {
    'title':'Film1',
    'uploader':'user1',
    'time':'123'
    },
    {
    'title':'film2',
    'uploader':'user2',
    'time':'1234'
    },
    {
    'title':'film3',
    'uploader':'user3',
    'time':'3456'
    },
    {
    'title':'film4',
    'uploader':'user4',
    'time':'444'
    },
    {
    'title':'film5',
    'uploader':'user5',
    'time':'24234'
    },
    {
    'title':'film6',
    'uploader':'user6',
    'time':'123'
    },
]

for (let vid of video_catalog) {
    //create new instance of Video. We will spread of Object.values array as args
    // into cunstructor function 
    videoElem = new Video(...Object.values(vid))
    videoElem.watch()
    //add create objec to the catalog as instance of Video object
    vid.videoElem = videoElem
    console.log(vid)
}