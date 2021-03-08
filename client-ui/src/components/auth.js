import React, {useState, useEffect} from 'react';
import {Link} from "react-router-dom";
import axios from 'axios';
import {Redirect} from 'react-router-dom';
import {connect} from 'react-redux';


function Auth(props) {
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
        axios.post(`http://localhost:8001/menu/token/`, {
            'username': login,
            'password': password
        }).then((response) => {
            alert(response.data.access);
            props.addToken(response.data.access);
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
                        <span className="heading">Авторизация</span>
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
                            <div className="main-checkbox">
                                <input type="checkbox" value="none" id="checkbox1" name="check"/>

                            </div>
                            <button type="submit" className="btn btn-default">ВХОД</button>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    )
}

export default connect(
    store => (
        {
            getStore: store
        }
    ),
    dispatch => (
        {
            addToken: (token) => {
                dispatch({type: 'ADD_TOKEN', payload: token})
            }
        }
    )
)(Auth);