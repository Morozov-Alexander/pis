import React, {useEffect, useState} from 'react';
import axios from 'axios';


function EditWorker({match}) {
    const workerSlug = match.params.slug;
    const [companies, setCompany] = useState([]);
    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8001/menu/companies_json"
        }).then(response => {
            setCompany(response.data)
        })

    }, [])

    const [firstName, setName] = useState('');
    const [secondName, setSecondName] = useState('');
    const [slug, setSlug] = useState('');
    const [company, setComp] = useState('');

    console.log(companies);


    const changeFirstName = (e) => {
        setName(e.target.value);
        console.log(e.target.value);
    }

    const changeSecondName = (e) => {
        setSecondName(e.target.value);
        console.log(e.target.value);
    }

    const changeSlug = (e) => {
        setSlug(e.target.value);
        console.log(e.target.value);
    }

    const changeCompany = (e) => {
        setComp(e.target.value);
        console.log(e.target.value);
    }
    const onSubmit = (e) => {
        e.preventDefault();
        axios.put(`http://127.0.0.1:8001/menu/workers_json/${workerSlug}`, {
            'first_name': firstName,
            'second_name': secondName,
            'slug': slug,
            'company': company
        }).then(response => {
            if (response.status == 201) {
                alert('Работник успешно обновлён');
            } else {
                alert('Повезло повезло...');
            }

        })
    }
    return (
        <form className="rounded" onSubmit={onSubmit}
              style={{background: 'rgba(0,0,0,.5)'}}>
            <input type="hidden" name="csrfmiddlewaretoken"
                   value="us4oMnVKe9OmbyklQ0wZUNOxEyid4UuddkhQ4ocRN0Ur6ktRxLOULNT0sNfUP04f"/>

            <p><label className="inline_label"></label> <input type="text" name="first_name"
                                                               value={firstName}
                                                               onChange={changeFirstName}
                                                               className="form-control mr-sm-2"
                                                               placeholder="Имя работника" maxLength="100"
                                                               required id="id_first_name"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="second_name"
                                                               value={secondName}
                                                               onChange={changeSecondName}
                                                               className="form-input form-control mr-sm-2"
                                                               placeholder="Фамилия работника" maxLength="100"
                                                               required id="id_second_name"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <input type="text" name="slug"
                                                               value={slug}
                                                               onChange={changeSlug}
                                                               className="form-control mr-sm-2" placeholder="URL"
                                                               maxLength="100" required id="id_slug"/></p>
            <div className="row-form-errors"></div>

            <p><label className="inline_label"></label> <select name="company" onChange={changeCompany} required
                                                                id="id_company" value={company}>
                <option value="" selected>---------</option>
                {companies.map(company => (
                    <option value={company.id}>{company.name}</option>
                ))}
            </select></p>
            <div className="row-form-errors"></div>

            <button type="submit" className="btn btn-outline-light mr-sm-2">Сохранить</button>
        </form>

    )
}

export default EditWorker;