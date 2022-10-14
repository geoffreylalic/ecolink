function getPublications() {
    return fetch("http://localhost:8002/publications/")
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


function createPublication() {
    return fetch("http://localhost:8002/publications/")
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

export default { getPublications, getSupplies, getDemands, createPublication, getDetailPublication}