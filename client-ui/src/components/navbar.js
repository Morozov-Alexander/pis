import {Link} from 'react-router-dom';

function Navbar() {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <button className="navbar-toggler" type="button" data-toggle="collapse"
                        data-target="#navbarTogglerDemo03"
                        aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <Link className="navbar-brand" to={{pathname:`/main`}}>Домой</Link>

                <div className="collapse navbar-collapse" id="navbarTogglerDemo03">

                    <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li className="nav-item active">
                            <Link to={{pathname : `/main/companies`}} className="dropdown-item">Компании<span
                                    className="sr-only">(current)</span></Link>
                        </li>
                       <li className="nav-item active">
                            <Link to={{pathname : `/main/types`}} className="dropdown-item">Типы изданий<span
                                    className="sr-only">(current)</span></Link>
                        </li>
                        <li className="nav-item active">
                            <Link to={{pathname : `/main/workers`}} className="dropdown-item">Работники<span
                                    className="sr-only">(current)</span></Link>
                        </li>
                    </ul>
                    <form className="form-inline my-2 my-lg-0">
                        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Зарегестрироваться
                        </button>
                    </form>
                </div>
            </nav>
        </div>
    );
}

export default Navbar;