import './hello.css'
import './HelloClass'
const Hello = () => {
    const users = [
        {
        name:"mary",
        email:"mary@fmail.com"
        },
        {
            name:"pary",
            email:"pary@fmail.com"
        },
        {
            name:"dary",
            email:"d@fmail.com"
        },
    ]
    const returnUsers = users.map(item => {
        return(
            <div className='title'>
            
                <h4>{item.name}</h4>
                <h4>{item.email}</h4>
            </div>
        )
    })
    console.log(returnUsers)


    return(
        <div>
        <h1>Hello1</h1>
        {
            returnUsers
        }
        
        </div>
    
    )
}

export default Hello