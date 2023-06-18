import React from 'react';
import ToDoList from './ToDoList';
import AddToDoForm from './AddToDoForm'
import { useState } from 'react'
import 'tachyons'



const ToDoApp = () => {

    const [toDoList, updateToDo] = useState ([
                                        'Create ToDo',
                                        'Delete Todo',
                                        'a',
                                        'b'
                                    ])

    let props={toDoList:toDoList, callBack:updateToDo}

    return (
        <div>
        <h1 class="f8 bold center mw5">ToDo's</h1>
            <ToDoList props = {props} />
            <AddToDoForm props = {props} />
        </div>
    )
}
export default ToDoApp

