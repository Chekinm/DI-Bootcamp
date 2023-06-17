import  React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { useRef } from 'react';
import './RandomQuoteApp.css';
import quotes from './static/QuotesDatabase';
import _ from 'lodash'; 
import { CSSTransition } from 'react-transition-group';


const RandomQuoteApp = (props) => {
    // I shuffle array of qotes and take it one by one
    // to store an index we use useRef  hook.
    // shuffled array also stored in as useRef Hook
    // once we get all the quote from array
    // we reshuffle it and reset index to quotes array lenght

    const index = useRef();
    const shuffledQuotes = useRef();
    useEffect (()=> {
        shuffledQuotes.current = _.shuffle(quotes)
        index.current = quotes.length - 1 
    },[])

    const [quote, setQuote] = useState({
            text:'Every quote on the internet is a lie',
            author:'Lenin V.I',
            color: 'green',
    })

    const changeQuote = () => {
        
        if (!index.current) {    // quotes finished - will reshuffle quotes
            shuffledQuotes.current = _.shuffle(quotes)
            index.current = quotes.length - 1
        }   
        
        //take new quotes
        let newQuote = shuffledQuotes.current[index.current] 
        index.current = index.current - 1

        // use state manager to update quote
        setQuote({
            text: newQuote.quote,
            author:(newQuote.author)? newQuote.author: 'unknown',
            color: `rgb(${Math.floor(Math.random()*100)},
                    ${Math.floor(Math.random()*100)},
                    ${Math.floor(Math.random()*100)})`, 
                    //dark colors (0,100) to be more constrast 
         })
    }

    useEffect(() =>{
        //this props callback pass our current random color to parent
        // to set background of quote
        props.setColor(quote.color)
    })
    
    return (
        <div className='quote' style={{color:quote.color, transition: 'background-color 1.5s ease-in-out'}}> 
            <div  className="fadeIn" key={index.current}>
                <div  className='text'>"{quote.text}"</div>
                <div className='author'>- {quote.author} -</div>
            </div>
            <button className='button' onClick={changeQuote} style={{backgroundColor:quote.color, transition: 'background-color 1.5s ease-in-out'}}>
                Next quote
            </button>
        </div>
    )
}

export default RandomQuoteApp