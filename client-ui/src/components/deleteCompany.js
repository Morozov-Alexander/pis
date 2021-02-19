import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Redirect} from 'react-router';


function DeleteCompany({match}) {
    const slug = match.params.slug;
    axios.delete(`http://127.0.0.1:8001/menu/companies_json/${slug}`).then(
        response => {
            if (response.status === 200) {
                alert('Компания успешно удалёна');
            } else {
                alert('Повезло повезло...');
            }
        }
    )

    return(
        <div>

        </div>
    )

}

export default DeleteCompany;