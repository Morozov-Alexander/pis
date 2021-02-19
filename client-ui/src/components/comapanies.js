import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";

function Companies({match}) {

    const [company, setCompany] = useState([]);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8001/menu/companies_json"
        }).then(response => {
            setCompany(response.data)
        })

    }, [])
    return (
        <div>
            <center>
            <Link to={{pathname: `/main/add_company`}}>Добавить компанию</Link>
            <table>

                <tr>
                    <th>Название компании</th>
                    <th>URl</th>
                    <th>Редактировать</th>
                    <th>Удалить</th>
                </tr>
                {company.map(company => (
                    <tr>
                        <td>{company.name}</td>
                        <td>{company.slug}</td>
                        <td><Link to={{pathname: `/main/edit_company/${company.slug}`}}>Изменить</Link></td>
                        <td><Link to={{pathname: `/main/delete_company/${company.slug}`}}>Изменить</Link></td>
                    </tr>
                ))}

            </table>
                </center>
        </div>

    )
}

export default Companies;