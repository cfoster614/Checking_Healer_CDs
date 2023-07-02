/* For radio inputs since I have taken away the actual radio button itself
and am just using pictures of the bosses */

let cachedSpells = [];


async function getSpellInfo() {
    //Query the api for spell info.
    if (cachedSpells.length === 0) {
        const resp = await axios.get('http://127.0.0.1:5000/api.healer_cds.com/spells');
        cachedSpells = createNewSpellsClasses(resp.data.spells)
    }
    return cachedSpells
}


function createNewSpellsClasses(arr) {
    //Turn the array of objects of spells into their own individual classes.
    //Makes it easier to access them later on.
    let id;
    let name;
    let icon;

    //Create a new list that has all of the new Spell classes.

    for (let i = 0; i < arr.length; i++) {
        for (let key in arr[i]) {
            if (key.includes('id')) {
                id = (arr[i][key])
            }
            if (key.includes('name')) {
                name = (arr[i][key])
            }
            if (key.includes('icon')) {
                icon = (arr[i][key])
            }
        }
        const newSpell = new Spell(id, name, icon)
        cachedSpells.push(newSpell)
    }
    return cachedSpells
}


getSpellInfo()


