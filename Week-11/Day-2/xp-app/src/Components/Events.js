import { Component } from "react";
import './Events.css'

class Events extends Component {

    constructor() {
        super()
        this.state = {
            isToggleOn : true
        }
    }
    
    


    clickMe = () => {
        alert('I was clicked')
    }

    changeToggel = () => {
        this.setState({isToggleOn: !this.state.isToggleOn})
    } 

    handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            alert(`The Enter key was pressed, your input is: ${e.target.value}`)
        }
    }
    
    render(){
        return(
        <div> 
            <div>
                <button onClick={this.clickMe}>Click me</button>
            </div>
            <input type="text" onKeyDown={this.handleKeyDown}></input>
            <div>
            <div className="toggle"> Toggle me
                <button className="toggle" onClick={this.changeToggel}> {this.state.isToggleOn ? 'ON' : 'OFF'} </button>
            </div>
            </div>
        </div>
        )
    }
}
export default Events