import {combineReducers} from "redux";
import token from "./token";
import {routerReducer} from 'react-router-redux';

export default combineReducers({
    routing: routerReducer,
    token
})