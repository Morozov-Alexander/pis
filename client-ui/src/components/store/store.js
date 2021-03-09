import {combineReducers} from "redux";
import token from "./token";
import {routerReducer} from 'react-router-redux';
import refresh_token from "./refresh_token";

export default combineReducers({
    routing: routerReducer,
    token,
    refresh_token
})