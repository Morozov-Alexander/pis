import React from 'react';
import axios from 'axios';

class Add_type extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: '',
            slug: ''
        }
        this.onChangeSlug = this.onChangeSlug.bind(this)
        this.onChangeType = this.onChangeType.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    onSubmit(event) {
        axios.post("http://127.0.0.1:8001/menu/all_types_json", this.state).then(
            response => {
                if (response.status === 201) {
                    alert('Тип успешно добавлен')
                } else {
                    alert('Повезло повезло...')
                }

            }
        )
        event.preventDefault();
    }

    onChangeType(event) {
        this.setState({type: event.target.value})
        console.log(event.target.value);
    }

    onChangeSlug(event) {
        this.setState({slug: event.target.value})
        console.log(event.target.value);
    }

    render() {
        return (
            <form className="rounded" onSubmit={this.onSubmit}
                  style={{background: 'rgba(0,0,0,.5)'}}>
                <input type="hidden" name="csrfmiddlewaretoken"
                       value="014aBdEKZGaEXJb3Ox4hu35wAZLh3pbcJThCTeVRyxgJSvkzvimcl3aZoeIYOvLe"/>

                <p><label className="inline_label"></label> <input type="text" name="type"
                                                                   value={this.state.type}
                                                                   onChange={this.onChangeType}
                                                                   className="form-input form-control mr-sm-2"
                                                                   placeholder="Type" maxLength="100" required
                                                                   id="id_slug"/></p>
                <div className="row-form-errors"></div>

                <p><label className="inline_label"></label> <input type="text" name="slug"
                                                                   value={this.state.slug}
                                                                   onChange={this.onChangeSlug}
                                                                   className="form-input form-control mr-sm-2"
                                                                   placeholder="URL" maxLength="100" required
                                                                   id="id_slug"/></p>
                <input className="btn btn-outline-danger" type="submit"/>
            </form>
        );
    }

}

export default Add_type;