export default function token(state = [], action) {
    switch (action.type) {
        case  'ADD_TOKEN':
            return [
                ...state, action.payload
            ]
        case 'DELETE_TOKEN':
            return []
        default:
            return state
    }
}