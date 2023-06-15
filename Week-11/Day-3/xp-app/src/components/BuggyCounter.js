import { Component } from "react";


class BuggyCounter extends Component {

    constructor() {
        super();
        this.state = {
            counter: 0
        }
    }

    handleClick = () => {
        let newCounter = this.state.counter + 1; 
        this.setState({counter: newCounter})

    }


    render() {
        if (this.state.counter > 5) {
            throw new RangeError("correct out of range counter")
        } else {

        return(
            <h1 onClick={this.handleClick}>Buggy Counter = {this.state.counter}</h1>
        )
        }
    }

}

export default BuggyCounter