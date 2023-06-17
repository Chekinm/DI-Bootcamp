import React from "react";
import DailyApp from './DailyApp'
import AnswersApp from "./AnswersApp";
import './MainPage.css'
import { useState } from "react";

const MainPage = () => {
    const [data, setData] = useState({ 
            firstName : '',
            lastName : '',
            favoriteColor : '',
            beer : '',
            wine : true,
            vodka : '',
            gender : ''
    })


    return (
        <div>
            <div className='form'>
                <DailyApp callBack={setData}/>
                <br/>
            </div>
            <hr/>
            <div className='answers'>
                <AnswersApp  data={data}/>
            </div>


        </div>

    )
} 
export default MainPage