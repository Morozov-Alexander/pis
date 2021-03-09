import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";
import {connect} from 'react-redux';
import refresh_token from "./store/refresh_token";

function AddCompany(props) {
    const [myName, setName] = useState('')
    const [mySlug, setSlug] = useState('')

    const RefreshToken = (r_token) => {
        const header = {
            Authorization: 'Bearer ' + r_token
        }
        axios.post(`http://127.0.0.1:8001/menu/companies_json`, {"name": myName, "slug": mySlug}, {
            headers: header
        }).then(
            response => {
                if (response.status === 201) {
                    alert('Компания успешно добавлена');
                }
            }
        ).catch(err => {
                alert('Авторизируйтесь');
            }
        )
    }


    const onSubmit = (e) => {
        e.preventDefault();
        const header = {
            'Authorization': 'Bearer ' + props.getStore.token[0],
        }
        axios.post(`http://127.0.0.1:8001/menu/companies_json`, {"name": myName, "slug": mySlug}, {
            headers : header
        }).then(
            response => {
                if (response.status === 201) {
                    alert('Компания успешно добавлена');
                }
            }
        ).catch(err => {
            if (err.data.status === 401 && props.getStore.token[0]) {
                RefreshToken(props.getStore.refresh_token[0]);
            } else {
                alert('Авторизируйтесь');
            }

        })

    }

    const changeName = (e) => {
        setName(e.target.value);
        console.log(e.target.value);
    }

    const changeSlug = (e) => {
        setSlug(e.target.value);
        console.log(e.target.value);
    }

    return (
        <form className="rounded" onSubmit={onSubmit}
              style={{background: 'rgba(0,0,0,.5)'}}>
            <input type="hidden" name="csrfmiddlewaretoken"
                   value="014aBdEKZGaEXJb3Ox4hu35wAZLh3pbcJThCTeVRyxgJSvkzvimcl3aZoeIYOvLe"/>

            <p><label className="inline_label"></label> <input type="text" name="type"
                                                               value={myName}
                                                               onChange={changeName}
                                                               className="form-input form-control mr-sm-2"
                                                               placeholder="Название компании" maxLength="100" required
                                                               id="id_slug"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="slug"
                                                               value={mySlug}
                                                               onChange={changeSlug}
                                                               className="form-input form-control mr-sm-2"
                                                               placeholder="URL" maxLength="100" required
                                                               id="id_slug"/></p>
            <input className="btn btn-outline-danger" type="submit"/>
        </form>
    )
}

export default connect(
    store => ({
        getStore: store
    })
)(AddCompany);