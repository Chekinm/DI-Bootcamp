import { Component } from "react";

class Phone extends Component {

    constructor() {
        super()
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "orange",
            year: 2020,
        };
    }
    
    


    changeColor = () => {
        this.setState({color:"blue"})
    }
    
    render(){
        return(
        <div> 
            <h1>My phone is a {this.state.brand}.</h1>
            It is a <span style={{color:this.state.color}}>{this.state.color}</span> {this.state.model} from {this.state.year}
            <p><button onClick={this.changeColor}>Change color to blue</button></p>

        </div>
        )
    }
}
export default Phone