import { Component } from "react";




class Color extends Component {

    constructor() {
        super()
        this.state = {
            favoriteColor : "red",
            st: "color:red"
        };
    }
    
    


    componentDidMount( prevProp, prevState) {
        setTimeout(()=>this.setState({
            favoriteColor : "yellow"}), 5000)
    }

    changeColor = () => {
        this.setState({favoriteColor:"blue"})
    }
    
    render(){
        return(
        <div> 
            <h1>My favorite Color is a <span style={{color:this.state.favoriteColor}}>{this.state.favoriteColor}</span>.</h1>
           
            <p><button onClick={this.changeColor}>Change my mind</button></p>

        </div>
        )
    }
}
export default Color