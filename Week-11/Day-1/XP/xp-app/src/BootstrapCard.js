import React from 'react'


const BootstrapCard = (props) => {
    const {title, imageUrl, buttonLabel, buttonUrl, description} = props.props
    return (
    
    <div className="card m-5" style={{width: '30rem'}}>
        <img className="card-img-top" src={imageUrl} alt="Card image cap1" />
        <div className="card-body">
            <h5 className="card-title">{title}</h5>
            <p className="card-text">{description}</p>
            <a href={buttonUrl} className="btn btn-primary">{buttonLabel}</a>
        </div>
    </div>
)
}

export default BootstrapCard