import React from "react";
import { useState } from "react";
import { useEffect } from "react";


const Counter = () => {
    const [count, setCount] = useState(0)
    const [name, setName] = useState('')

    useEffect(() => {
        console.log(count,'imherer');

    },[name, count])

    const handleClick = () => {
        setCount (count + 1)
        console.log(count)
    }

    return (
        <div>
            <h1>Counter</h1>
            <h2>{count}</h2>
            <button onClick={handleClick}>Add</button>
        </div>

    )
}

export default Counter