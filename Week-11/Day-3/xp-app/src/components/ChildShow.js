import { Component } from "react";
import Child from "./Child";

class ChildShow extends Component {
    
    constructor() {
        super()
        this.state = {show: true}
    }

    hideMe = () => {
        console.log(this.state)
        this.setState({show:false})
    }

    render() {
        if (this.state.show) {
            return(
                <div>
                    <Child />
                    <button onClick={this.hideMe}>Hide Me</button>
                </div>
            )
        } else {
            return (<h1>Child is hidden</h1>)
        }     
    }
}

export default ChildShow