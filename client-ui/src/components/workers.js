import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";

function Workers({match}) {
    const [workers, setWorker] = useState([])
    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8001/menu/workers_json`
        }).then(response => {
            setWorker(response.data)
        })

    }, [])

    return (
        <div>
            <center>
                <Link to={{pathname: `/main/add_worker`}}>Добавить Работника</Link>
                <table>

                    <tr>
                        <th>Имя работника</th>
                        <th>Фамилия работника</th>
                        <th>Работа</th>
                        <th>URl</th>
                        <th>Редактировать</th>
                        <th>Удалить</th>
                    </tr>
                    {workers.map(worker => (
                        <tr>
                            <td>{worker.first_name}</td>
                            <td>{worker.second_name}</td>
                            <td>{worker.company}</td>
                            <td>{worker.slug}</td>
                            <td><Link to={{pathname: `/main/edit_worker/${worker.slug}`}}>Изменить</Link></td>
                            <td><Link to={{pathname: `/main/delete_worker/${worker.slug}`}}>Удалить</Link></td>

                        </tr>
                    ))}

                </table>
            </center>
        </div>
    )

}

export default Workers;