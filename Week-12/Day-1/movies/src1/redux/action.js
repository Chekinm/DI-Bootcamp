export const DETAIL = 'DETAIL'

export const showDetails = (item) => {
    return {
        type: 'DETAIL',
        payload: item
    }
}