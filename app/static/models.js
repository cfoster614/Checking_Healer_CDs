class Spell {
    /* Class for creating a new Spell from the API. */
    constructor(id, name, icon) {
        this.id = id;
        this.name = name;
        this.icon = icon;
    }

    toString() {
        return this.name
    }
}

function filterClass(obj) {
    return obj.map(element => element.toString())
}

