import React from 'react'
import './Modal.css' 

class Modal extends React.Component {

    componentWillUnmount() {
        //Check is 
        console.log('Modal has closed')
    }
    render() {
        // we get from parent error state and 
        // callback function to restore form error state
        // so onCLick will exicute function from parent
        // which set its' state to non error 
        return(
            <div className='modal-background'>
                <div className='modal-body'> 
                    {this.props.passObj.state.error.toString()}
                    <br/>
                    <button onClick={this.props.passObj.callback} >Close</button>
                </div>
            </div>)
    
    }
}
export default Modal
