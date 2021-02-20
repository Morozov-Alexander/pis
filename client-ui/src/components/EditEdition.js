import React, {useEffect, useState} from 'react';
import axios from 'axios';


function EditEdition({match}) {
    const editionSlug = match.params.slug;
    const [workers, setWorker] = useState([]);
    const [types, setType] = useState([]);

    const [name_of_the_edition, setName] = useState('');
    const [start_data, setStart] = useState('');
    const [end_data, setEnd] = useState('');
    const [slug, setSlug] = useState('');
    const [type, setTyp] = useState('');
    const [worker, setWorkers] = useState([]);
    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8001/menu/workers_json"
        }).then(response => {
            setWorker(response.data)
        })

    }, [])

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8001/menu/all_types_json"
        }).then(response => {
            setType(response.data)
        })

    }, [])


    const changeName = (e) => {
        setName(e.target.value);
        console.log(e.target.value);
    }

    const changeStart = (e) => {
        setStart(e.target.value);
        console.log(e.target.value);
    }

    const changeEnd = (e) => {
        setEnd(e.target.value);
        console.log(e.target.value);
    }

    const changeWorker = (e) => {
        setWorkers(Array.from(e.target.selectedOptions, option => option.value));
        console.log(Array.from(e.target.selectedOptions, option => option.value));
    }

    const changeSlug = (e) => {
        setSlug(e.target.value);
        console.log(e.target.value);
    }

    const changeType = (e) => {
        setTyp(e.target.value);
        console.log(e.target.value);
    }
    const onSubmit = (e) => {
        e.preventDefault();
        const temp = {
            'name_of_the_edition': name_of_the_edition,
            'start_data': start_data,
            'end_data': end_data,
            'slug': slug,
            'type': type,
            'worker': worker}
            console.log(temp);
        axios.put(`http://127.0.0.1:8001/menu/editions_json/${editionSlug}`, {
            'name_of_the_edition': name_of_the_edition,
            'start_data': start_data,
            'end_data': end_data,
            'slug': slug,
            'type': type,
            'worker': worker
        }).then(response => {
            if (response.status == 201) {
                alert('Издание успешно обновлено');
            } else {
                alert('Повезло повезло...');
            }

        })
    }
    return (
        <form className="rounded"
              style={{background: `rgba(0, 0, 0, .5)`}} onSubmit={onSubmit}>
            <input type="hidden" name="csrfmiddlewaretoken"
                   value="wToJhAdxqcrrRm2BNW8k4EqmIJEJHTyifLBbzBuEZ3xwM8b7uHqfVEvPwYBqsZ8k"/>

            <p><label className="inline_label"></label> <input type="text" name="name_of_the_edition"
                                                               value={name_of_the_edition}
                                                               onChange={changeName}
                                                               className="form-control mr-sm-2"
                                                               placeholder="Издание" maxLength="100" required
                                                               id="id_name_of_the_edition"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="start_data"
                                                               value={start_data}
                                                               onChange={changeStart}
                                                               className="form-input form-control mr-sm-2"
                                                               placeholder="Начало подписки" required
                                                               id="id_start_data"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="end_data"
                                                               value={end_data}
                                                               onChange={changeEnd}
                                                               className="form-control mr-sm-2"
                                                               placeholder="Конец Подписки" required
                                                               id="id_end_data"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="slug"
                                                               value={slug}
                                                               onChange={changeSlug}
                                                               className="form-input form-control mr-sm-2"
                                                               placeholder="URL" maxLength="50" required
                                                               id="id_slug"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <select name="worker" required id="id_worker" multiple={true}
                                                                value={worker} onChange={changeWorker}>
                {workers.map(worker => (
                    <option value={worker.id}>{worker.first_name}</option>
                ))}

            </select></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <select name="type" required id="id_type" value={type}
                                                                onChange={changeType}>
                <option value="" selected>---------</option>
                {types.map(type => (
                    <option value={type.id}>{type.type}</option>
                ))}
            </select></p>
            <div className="row-form-errors"></div>

            <button type="submit" className="btn btn-outline-light mr-sm-2">Сохранить</button>
        </form>
    )
}

export default EditEdition;