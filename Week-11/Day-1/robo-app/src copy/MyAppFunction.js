import React from 'react'
import './MyFunctionApp.css'

const MyAppFunction = (props) => {
    return (
        <div className="App">
            <header className="App-header">
             <h1>form MyAPP11111</h1>
             <h3>{props.MyAppFunctionProps}</h3>
            </header>
        </div>
    )
} 

// class MyApp extends Component {
//     render() {
//         return (
//         <h1>Hello from MyApp</h1>
//     )
//     }
// }

export default MyAppFunction