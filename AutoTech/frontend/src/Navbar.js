export default function Navbar(){

    return( <nav className="nav">
        <ul>
            <li>
                <a href="/statistics">Статистики</a>
                <li></li>
                <a href="/newCard">Нова работна карта</a>
                <li></li>
                <a href="/search">Търсене</a>
            </li>
        </ul>
    </nav>
    )
}