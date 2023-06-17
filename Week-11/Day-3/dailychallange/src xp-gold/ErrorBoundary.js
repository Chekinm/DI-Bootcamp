import React from 'react'
import Modal from './Modal'

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            hasError:false,
            error:null
        }
    }

    static getDerivedStateFromError(error) {
        return ({
            hasError:true,
            error:error
        })
    }

    handleReturnClick = () => {
        // Reset error state and return to pre-error state
        this.setState({ 
            hasError: false, 
            error: null});
      };

    render () {
        if (this.state.hasError) {
            //create an object to pass as props to error Modal
            //add there a handleReturn function
            // which will reset  state of this Error boundary
            const passObj = {
                state:this.state,
                callback:this.handleReturnClick
            }
            return(
                <div>
                    <Modal passObj={passObj} />                    
                </div>
            )
        }    
        return this.props.children
    }
}

export default ErrorBoundary