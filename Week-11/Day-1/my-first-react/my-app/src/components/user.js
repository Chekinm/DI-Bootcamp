import React from "react";


class UserClass extends React.Component {


    render(){
    const {userinfo} = this.props;
    const {id, name, email, username, phone} = userinfo;
    return (
        <div>
            <img src={`https://robohash.org/${id}?size=150x150`}/>
            <h2>{name}</h2> 
            <h2>{email}</h2>

            <h2>{username}</h2>

            <h2>{phone}</h2>



        </div>
    )
    }
}
export default UserClass