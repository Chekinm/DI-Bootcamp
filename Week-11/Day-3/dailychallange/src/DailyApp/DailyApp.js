import React from 'react'

class AppForm extends React.Component {

    constructor() {
        super()
        this.state = {
            firstName : '',
            lastName : '',
            favoriteColor : '',
            beer : '',
            wine : '',
            vodka : '',
            gender : ''
        }
    }


    handleSubmit = (e) => {
        console.log(this.props)
        e.preventDefault()
        const { firstName, lastName, favoriteColor, beer, wine, vodka, gender } = this.state
        // console.log(firstName, lastName, favoriteColor, beer, wine, vodka, gender);
        this.props.callBack(this.state)
        
        // we can submit data using next, but it will 
        // deletet all data

        //e.target.submit()
    }

    handleChange = (e) => {
        const value = (e.target.type === 'checkbox')
                ?e.target.checked
                :e.target.value;
        this.setState({[e.target.name]:value});
        this.props.callBack(this.state);
    }




    render() {
        return(
            <div>
            <h1>My Form</h1>
            <form onSubmit={this.handleSubmit} method='get'>
                First name: <input 
                                type='text' 
                                name='firstName'
                                onChange={this.handleChange}
                />
                <br/>
                Last name: <input 
                            type='text' 
                            name='lastName'
                            onChange={this.handleChange}
                            />
                <br/>
                <select 
                    name='favoriteColor' 
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
                    name='wine' 
                    onChange={this.handleChange} 
                />
                <br/>

                Vodka <input 
                    type='checkbox' 
                    name='vodka' 
                    onChange={this.handleChange} 
                />
                <br/>
             


            <div onChange={this.handleChange}>
                <input type='radio' value='male' name='gender' />Male
                <input type='radio' value='female' name='gender' />Female
                <input type='radio' value='other' name='gender' />Other
            </div>       
            
            <br/>
            <input type='submit' value='Submit' />
            <br/>

            </form>
            </div>
        )  
    }
}

export default AppForm