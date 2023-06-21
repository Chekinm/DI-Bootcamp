
const Favorites = () => {
    const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT
    console.log(PROXY_PORT)
    return  (
        <h1>{PROXY_PORT}</h1>        
    )
}

export default Favorites