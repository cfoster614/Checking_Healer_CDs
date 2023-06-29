let textInputId = 0

function addSpellHandler() {
    /* Create a new  text input to add another healer cd/timer. textInputId is used to create a unique id for each input */
    const newSpellInput = ($('<input>', {type: 'text', class:'spells', id:`spells-input-${textInputId}`}));
    const newTimerInput = ($('<input>', {type: 'text', class:'timers'}));
    $('#spell-form input.spells').each(function() {
        newSpellInput.insertAfter($(this));
        textInputId += 1
    })
    
    $('#timer-form input.timers').each(function() {
        newTimerInput.insertAfter($(this));
    })
}


function search(arr) {
    /* Search the filteredSpells array from showSuggestions function.
    Return true if the input val is in the array somewhere. */

    const searchText = $('input[type=text]').val()
    return arr.filter(element => element.toLowerCase().includes(searchText));
}

async function searchHandler(e) {
    /* When keypress is registered, await getSpellInfo for API in */
    const spellsObj = cachedSpells
    showSuggestions(spellsObj, e.key)
}

function showSuggestions(obj) {
    $('#spell-suggestions').empty()
  
    let spellNames = filterClass(obj, 'name')
    let filteredSpells = search(spellNames)

    console.log(filteredSpells)
    
    Object.keys(obj).forEach((key) => {
        const spell = obj[key];
        console.log(spell.name)
        if (filteredSpells.includes(spell.name)) {
            $('#spell-suggestions').append(`<li><img src=${spell.icon}>${spell.name}</li>`);
        }
    });
    
}

function useSuggestion(e) {
    // const spellInput = $(`input[id=spells-input-${textInputId}]`)
    const suggestionText = e.target.innerText
    console.log(e.target.innerText)
    $('#spell-suggestions').empty();
    $(`#spells-input-${textInputId}`).val(e.target.innerText)
}