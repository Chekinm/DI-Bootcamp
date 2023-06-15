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
            console.log(this.state.error, this.state.errorInfo)
            return(
                <div>
                    <h1>Huston we have a problem!</h1>
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
//     constructor(props) {
//         console.log(props.children)
//         super(props);
//         this.state = { 
//             hasError: false};
//         }
    
//     static getDerivedStateFromError(error) {
//         // Update state so the next render will show the fallback UI.
//         console.log('?????????????????')
//         return { hasError: true };
//         }


//     componentDidCatch(error, info) {
//     // Example "componentStack":
//     //   in ComponentThatThrows (created by App)
//     //   in ErrorBoundary (created by App)
//     //   in div (created by App)
//     //   in App
//         console.log('ERRRRRRRRRR', error, info.componentStack);
//     }

//     render() {
//         console.log('im in render')
//         if (this.state.hasError) {
//             return this.props.fallback;
//         } else {
//             return this.props.children
//         }
//     }
// }

export default ErrorBoundary