export default function refresh_token(state= [], action)
{
    if (action.type === 'ADD_REFRESH_TOKEN'){
        return [...state, action.payload];
    }
    else{
        return state;
    }
}