import React, {useState, useEffect} from 'react';
import {Link} from "react-router-dom";
import axios from 'axios';
import {Redirect} from 'react-router-dom'



function Registration({match}) {
    const [login, setLogin] = useState('')
    const [password, setPassword] = useState('')
    const [redirect, setRedirect] = useState(false)

    const changeLogin = (e) => {
        setLogin(e.target.value);
        console.log(e.target.value);
    }

    const changePassword = (e) => {
        setPassword(e.target.value);
        console.log(e.target.value);
    }

    const onSubmit = (e) => {
        e.preventDefault();
        axios.post(`http://localhost:8001/menu/clients_json/`, {
            'username': login,
            'password': password
        }).then((response) => {
            alert('Регистрация прошла успешно');
        }).catch(err => {
            alert(`Неверный запрос ${err}`);
        })
    }
    if (redirect) {
        return <Redirect to={{pathname: `/main`}}/>
    }

    return (
        <div className="container">
            <div className="row">

                <div className="col-md-offset-3 col-md-6">
                    <form className="form-horizontal" onSubmit={onSubmit}>
                        <span className="heading">Регистрация</span>
                        <div className="form-group">
                            <input type="login" className="form-control" id="inputEmail" placeholder="Login"
                                   value={login}
                                   onChange={changeLogin}/>
                        </div>
                        <div className="form-group help">
                            <input type="password" className="form-control" id="inputPassword" placeholder="Password"
                                   value={password}
                                   onChange={changePassword}/>


                        </div>
                        <div className="form-group">
                            <Link to={{pathname: `/main/auth`}}>
                                <button type="submit" className="btn btn-default">Авторизоваться</button>
                            </Link>
                            <button type="submit" className="btn btn-default">Зарегистрироваться</button>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    )
}

export default Registration;