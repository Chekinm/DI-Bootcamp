import { Component } from "react";

class Garage extends Component {


    
    render(){
        return(
            <header>Who lives in my {this.props.size} Garage?</header>
        )
    }
}
export default Garage