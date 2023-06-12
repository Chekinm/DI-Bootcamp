import { Component } from "react";
import VoteLang from "./VoteLang";

class Voting extends Component {

    constructor() {
        super()
        this.state = {
            languages : [
                {name: "Php", votes: 0},
                {name: "Python", votes: 0},
                {name: "JavaSript", votes: 0},
                {name: "Java", votes: 0}
            ]
        }
    }
    
    
    handleClick = (e) => {
        this.setState({count: this.state.count + 1})
        
        console.log(this.state.count)
    }
    
    render(){
        return(
        <div>
            {this.state.languages.map((lang,ind) => {
                return <VoteLang lang={lang} key={ind} />
            })}
        </div>
        )
    }
}

export default Voting