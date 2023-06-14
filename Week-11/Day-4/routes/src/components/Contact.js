import { useParams } from "react-router-dom"


const Contact = (props) => {

    const params = useParams()
    console.log(params)
    return  (
        <h1>Contact</h1>
    )
}

export default Contact