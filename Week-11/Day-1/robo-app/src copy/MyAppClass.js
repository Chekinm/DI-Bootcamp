import {Component} from 'react'
import './MyAppClass.css' 

class MyAppClass extends Component {

    render() {
        return(
        <div>
            <h1 className='h1'>This from MyAppClass component P222222</h1>
            <h3 className='h1'>{this.props.MyAppClassProp}</h3>
        </div>
        )
    }
}

export default MyAppClass



