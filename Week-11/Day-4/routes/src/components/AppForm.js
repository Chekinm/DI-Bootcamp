import React from 'react'

class AppForm extends React.Component {

    constructor() {
        super()
        this.state = {
            firstname : '',
            lastname : '',
            color : '',
            isgo : ''
        }
    }

    handleSubmit = (e) => {
        e.preventDefault()
        const { firstname, lastname, color, isgo, gender } = this.state
        console.log(firstname, lastname, color, isgo, gender);
    }

    handleChange = (e) => {
        console.log([e.target.value]);
        const value = (e.target.type === 'checkbox')
                ?e.target.checked
                :e.target.value;
        this.setState({[e.target.name]:value});
    }




    render() {
        return(
            <div>
            <h1>My Form</h1>
            <form onSubmit={this.handleSubmit}>
                First name: <input 
                                type='text' 
                                name='firstname'
                                onChange={this.handleChange}
                />
                <br/>
                Last name: <input 
                            type='text' 
                            name='lastname'
                            onChange={this.handleChange}
                            />
                <br/>
                <select 
                    name='color' 
                    onChange={this.handleChange}
                    >
                    <option value='1'>Red</option>
                    <option value='2'>Blue</option>
                    <option value='3'>Green</option>
                </select>
                <br/>
                
                Is going <input 
                    type='checkbox' 
                    name='isgo' 
                    onChange={this.handleChange} 
                />
                <br/>
                <input type='submit' value='Submit' />
            <div onChange={this.handleChange}>
                <input type='radio' value='male' name='gender' />Male
                <input type='radio' value='female' name='gender' />Female
                <input type='radio' value='other' name='gender' />Other
            </div>
            
            
            </form>
            </div>
        )  
    }
}

export default AppForm