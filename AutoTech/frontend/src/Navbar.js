import { Link } from "react-router-dom"

export default function Navbar(){

    return( <nav className="nav">
        <ul>
            <ActiveLink to="/statistics">Статистики</ActiveLink>
            <ActiveLink to="/newCard">Нова работна карта</ActiveLink>
            <ActiveLink to="/search">Търсене</ActiveLink>   
        </ul>
    </nav>
    )
}

function ActiveLink({ to, children, ...props }){
    const path = window.location.pathname

    return(
        <li className={path === to ? "active" : ""}>
            <Link to={to} {...props}>{children}</Link>
        </li>
    )
}