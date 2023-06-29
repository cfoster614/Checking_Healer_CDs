class Spell {
    /* Class for creating a new Spell from the API. */
    constructor(id, name, icon) {
        this.id = id;
        this.name = name;
        this.icon = icon;
    }
}

function filterClass(arr, key) {
    /* Helper function for filtering the results of the API object. Can choose which key
    to filter by */
    const spellNames = [];
    for (let i = 0; i < arr.length; i++) {
        spellNames.push(arr[i][key])
    }
    return spellNames;
}

