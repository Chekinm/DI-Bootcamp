import React from 'react'
import './ToDo.css'



const ToDoApp = (props) => {
    console.log(props.props.toDoList)
    const handleSubmit = (e) => {
        e.preventDefault()
        if (e.target[0].value) {
            let newArr = props.props.toDoList.toSpliced(props.props.toDoList.length,0, e.target[0].value)
            props.props.callBack(newArr)
        }
    }
    return (
        <form method='#' onSubmit={handleSubmit}>
            <input className='input' type='text' name='newToDo' />
            <button className='button' type='submit'>Add to do</button>
        </form>
    )

}
export default ToDoApp