/* For radio inputs since I have taken away the actual radio button itself
and am just using pictures of the bosses */

let cachedSpells = [];

async function getSpellInfo() {
    //Query the api for spell info.
    if (cachedSpells.length === 0) {
        const resp = await axios.get('http://127.0.0.1:5000/api.healer_cds.com/spells');

        // filteredSpells = filterObj(resp.data.spells)
        cachedSpells = createNewSpellsClasses(resp.data.spells)

    }
    return cachedSpells
}


    function createNewSpellsClasses(arr) {
        //Turn the array of objects of spells into their own individual classes.
        //Makes it easier to access them later on.
        //Create a new list that has all of the new Spell classes.
        let filteredSpells = [];
        for (let i = 0; i < arr.length; i++) {
            const name = (arr[i]['name']);
            console.log(arr[i])
            if(!filteredSpells.includes(name)){
                const newSpell = new Spell((arr[i]['spell_id']), name, (arr[i]['icon']) );
                cachedSpells.push(newSpell);
                filteredSpells.push(name);

            }
        }
        return cachedSpells
    }


    getSpellInfo()
