import React from 'react'
import { useState  } from 'react';
import { useEffect } from 'react';
import WatchSVG from './WatchSVG';

const Clock = () => {
    const [time , setTime] = useState({
        year:'1970',
        month:'1',
        day:'1',
        hours:'0',
        minutes:'0',
        seconds:'0'
    })
  
    useEffect(()=>{
        setInterval(()=>updateTime(),1000)
    },[])

    const updateTime = () => {
       
       setTime (() => { 
        let currentTime = new Date()
        return { 
            year:currentTime.getYear() + 1900, // year is 1900 based
            month: currentTime.getMonth() + 1, // month is 0 based
            day: currentTime.getDate(),
            hours: currentTime.getHours(),
            minutes: currentTime.getMinutes(),
            seconds: currentTime.getSeconds() 
            } 
        })
    }
        
    return (
        <div className="App">
        <header className="App-header">
                <WatchSVG time = {time} />
        </header>
        </div>
    );
}


export default Clock
