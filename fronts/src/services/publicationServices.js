function getPublications(name, category, type) {
    return fetch(`http://localhost:8002/publications/?name=${name}&category=${category}&type=${type}`)
        .then((r) => {
            console.log("r teste")
            return r.json()
        }).then((r) => {
            return r
        }).catch(e => console.error(e))
}

function getDetailPublication(id) {
    return fetch(`http://localhost:8002/publications/${id}/`)
        .then((r) => {
            return r.json()
        }).then((r) => {
            return r
        }).catch(e => console.error(e))
}


function createPublication(data) {
    return fetch(`http://localhost:8002/publications/`, { method: 'POST', body: data })
        .then((r) => {
            return r.json()
        }).then((r) => {
            return r
        }).catch(e => console.error(e))
}

function getSupplies() {
    console.log("getSupplies")
}

function getDemands() {
    console.log("getDemands")
}

export default { getPublications, getSupplies, getDemands, createPublication, getDetailPublication }