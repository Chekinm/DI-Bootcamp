import React from 'react'
import 'tachyons'
import './ToDo.css'


const ToDoList = (props) => {
    console.log(props)

    const deleteToDo = (e) => {
        // create new arr with deleted clicked element
        let updatedArr = props.props.toDoList.toSpliced(e.target.getAttribute("name"),1)
        // send updated array to parent to rerender tree
        props.props.callBack(updatedArr)
    }
    return (
        <ul class="list">
        { props.props.toDoList.map((item,id) => {
            return <li class="mb3 pa2 ba bg-green br3" 
                        key={id} 
                        onClick={deleteToDo}  
                        name={id}>
                        <span strike hover-s>{item}</span>
                    </li>
            }
            )
        }
        </ul>
    )
}
export default ToDoList


