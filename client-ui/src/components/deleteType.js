import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {BrowserRouter as Router, Switch, Route,} from 'react-router-dom';
import {Redirect} from 'react-router';
import Types from './types';


function DeleteType({match}) {
    var validate = false;
    const slug = match.params.slug;
    console.log(slug)
    axios.delete(`http://127.0.0.1:8001/menu/all_types_json/${slug}`,).then(
        response => {
            if (response.status === 200) {
                alert('Тип успешно удалён');
            } else {
                alert('Повезло повезло...');
            }
        }
    )

}

export default DeleteType;