import { Component } from "react";


class ErrorBoundary extends Component{

    constructor(props) {
        super(props);
        this.state = { 
            hasError: false,
            error:'',
            errorIngo:''};
        }
    
    componentDidCatch(error, info) {
        
        this.setState({
            hasError: true, 
            error: error,
            errorInfo: info})
    }

    render() {
        
        if (this.state.hasError) {
            console.log('We catch it')
            return(
                <div>
                    <p> An error has occurred in this component.Reload this page</p>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                    {this.state.error && this.state.error.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                    </details>
                </div>
            )


        } else {
            console.log('no error')
            return this.props.children
        }
    }
}

export default ErrorBoundary