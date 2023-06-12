import { Component } from "react";
import Garage from "./Garage";

class Car extends Component {

    constructor () {
        super()
        this.state = {
            color:'Blue'
        }
    }
    
    render(){
        return(
            <div>
                <Garage size="small" />
                <header>{this.state.color} {this.props.props.name} lives in my garage!</header>
            </div>
        )
    }
}
export default Car