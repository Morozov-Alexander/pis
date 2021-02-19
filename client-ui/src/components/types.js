import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";

function Types({match}) {

    const [type, setType] = useState([]);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8001/menu/all_types_json"
        }).then(response => {
            setType(response.data)
        })

    }, [])
    return (
        <div>
            <Link to={{pathname: `/main/add_type`}}>Добавить тип</Link>
            <table>

                <tr>
                    <th>Тип издания</th>
                    <th>URl</th>
                    <th>Редактировать</th>
                    <th>Удалить</th>
                </tr>
                {type.map(type => (
                    <tr>
                        <td>{type.type}</td>
                        <td>{type.slug}</td>
                        <td><Link to={{pathname: `/main/edit_type/${type.slug}`}}>Изменить</Link></td>
                        <td><Link to={{pathname: `/main/delete_type/${type.slug}`}}>Изменить</Link></td>

                    </tr>
                ))}

            </table>
        </div>

    )
}

export default Types;