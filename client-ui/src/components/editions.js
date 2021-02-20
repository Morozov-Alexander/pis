import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";

function Editions({match}) {
    const [editions, setEdition] = useState([])
    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8001/menu/editions_json`
        }).then(response => {
            setEdition(response.data)
        })

    }, [])

    return (
        <div>
            <center>
                <Link to={{pathname: `/main/add_edition`}}>Добавить Издание</Link>
                <table>

                    <tr>
                        <th>Название издания</th>
                        <th>Дата начала подписки</th>
                        <th>Дата окончания подписки</th>
                        <th>URl</th>
                        <th>Тип</th>
                        <th>Работники</th>
                        <th>Редактировать</th>
                        <th>Удалить</th>
                    </tr>
                    {editions.map(edition => (
                        <tr>
                            <td>{edition.name_of_the_edition}</td>
                            <td>{edition.start_data}</td>
                            <td>{edition.end_data}</td>
                            <td>{edition.slug}</td>
                            <td>{edition.type}</td>
                            <td><select>
                                {(edition.worker).map(worker => (
                                    <option>{worker}</option>
                                ))}
                            </select></td>
                            <td><Link to={{pathname: `/main/edit_edition/${edition.slug}`}}>Изменить</Link></td>
                            <td><Link to={{pathname: `/main/delete_edition/${edition.slug}`}}>Удалить</Link></td>

                        </tr>
                    ))}

                </table>
            </center>
        </div>
    )

}

export default Editions;