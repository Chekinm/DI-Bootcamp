import React from 'react'

class AppForm extends React.Component {

    constructor() {
        super()
        this.state = {
            firstname : '',
            lastname : '',
            age: '',
            color : '',
            isgo : ''
        }
    }

    handleSubmit = (e) => {
        e.preventDefault()
        const { firstname, lastname, age, color, isgo, gender } = this.state
        console.log(firstname, lastname, age, color, isgo, gender);
        e.target.submit()
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
            <form onSubmit={this.handleSubmit} method='get'>
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
                
                Beer <input 
                    type='checkbox' 
                    name='beer' 
                    onChange={this.handleChange} 
                />
                <br/>

                Wine <input 
                    type='checkbox' 
                    name='Wine' 
                    onChange={this.handleChange} 
                />
                <br/>

                Vodka <input 
                    type='checkbox' 
                    name='vodka' 
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