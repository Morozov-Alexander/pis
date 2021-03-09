import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link, Redirect} from "react-router-dom";
import {connect} from 'react-redux';

function UpdateCompany(props) {
    const slug = props.match.params.slug;
    console.log(slug);
    const [myName, setName] = useState('');
    const [mySlug, setSlug] = useState('');
    const [flag, setFlag] = useState(false);

    const RefreshToken = (r_token) => {
        const header = {
            Authorization: 'Bearer ' + r_token
        }
        axios.put(`http://127.0.0.1:8001/menu/companies_json/${slug}`, {"name": myName, "slug": mySlug}, {
            headers: header
        }).then(
            response => {
                if (response.status === 201) {
                    alert('Компания успешно обновлена');
                    setFlag(true);
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
        axios.put(`http://127.0.0.1:8001/menu/companies_json/${slug}`,
            {
                "name": myName, "slug": mySlug
            }, {
                headers: header
            }).then(
            response => {
                if (response.status === 201) {
                    alert('Компания успешно обновлена');
                    setFlag(true);
                }
            }
        ).catch(err => {
            if (err.status === 401 && props.getStore.token[0]) {
                RefreshToken(props.getStore.refresh_token[0]);
            } else {
                alert('Авторизируйтесь ');
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

    if (flag) {
        return <Redirect to={`/main/companies`}/>
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
    }))(UpdateCompany);