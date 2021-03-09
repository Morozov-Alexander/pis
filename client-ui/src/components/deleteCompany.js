import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Redirect} from 'react-router-dom';
import {connect} from 'react-redux';

function DeleteCompany(props) {
    const slug = props.match.params.slug;
    const [flag, setFlag] = useState(false);

    const header = {
        Authorization: 'Bearer ' + props.getStore.token[0]
    }
    axios.delete(`http://127.0.0.1:8001/menu/companies_json/${slug}`, {headers: header}).then(
        response => {
            if (response.status === 200) {
                alert('Компания успешно удалёна');
            }
            setFlag(true);

        }
    ).catch(err => {
        if (err.status === 401 && props.getStore.token[0]) {
            RefreshToken(props.getStore.refresh_token[0]);
        } else {
            alert('Авторизируйтесь ');
            setFlag(true);
        }

    })

    if (flag) {
        return <Redirect to={`/main/companies`}/>
    }

    const RefreshToken = (r_token) => {
        const header = {
            Authorization: 'Bearer ' + r_token
        }
        axios.delete(`http://127.0.0.1:8001/menu/companies_json/${slug}`, {headers: header}).then(
            response => {
                if (response.status === 201) {
                    alert('Компания успешно удалена');
                }
            }
        ).catch(err => {
                alert('Авторизируйтесь');
            }
        )
    }

    return (
        <div>

        </div>
    )


}

export default connect(
    store => ({
        getStore: store
    }))(DeleteCompany);