import { Component } from 'react'

class CrashButton extends Component {
    constructor () {
        super()
        this.state = {text:JSON.stringify({'s':'s'})}
    }

    render () {
        const textSetter = () => {
            const crasher = { function: 'invalidJson who crash testSetter' };
            this.setState({text:{crasher}});
            console.log('im in textsetter', this.state.text)
        }
        console.log(this.state.text)
        return (
            <button onClick={textSetter}>
                Make a crash<span style={{display:'none'}}>{this.state.text}</span>
             </button>
        )
    }
    
}

export default CrashButton