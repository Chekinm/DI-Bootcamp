import { Component } from "react";


class CounterC extends Component {
    constructor () {
        super()
        this.state = {
            count: 0
        }
    }

    handleClick = () => {
        this.setState({count: this.state.count + 1})
        
        console.log(this.state.count)
    }

    // componentDidMount = () => {
    //     console.log('CounterC did mount');
    //   }
    
    
    render(){
        return(
        <div>
            <h1>CounterC</h1>
            <h2>{this.state.count}</h2>
            <button onClick={this.handleClick}>Add</button>
        </div>
        )
    }
}

export default CounterC