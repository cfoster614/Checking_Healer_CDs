/* Can use the functions found in apiQuery */

let textInputId = 1

function addSpellHandler() {
    /** 
     * Create a new  text input to add another healer cd/timer. 
     * textInputId is used to create a unique id for each input. 
     */
    $('.suggestions').remove();
    const newSpellInput = ($('<input>', { type: 'text', class: 'spells', id: `spells-input-${textInputId}` }));
    const newUl = ($('<ul>', { id: 'spell-suggestions', class: 'suggestions' }));
    const newDiv = ($('<div>', { class: 'suggestions-box', id: `suggestions-box-${textInputId}` }));

    newDiv.insertBefore($('.add-btn'));
    newDiv.append(newSpellInput, newUl);

    $('#timer-form').append($('<input>', { type: 'text', class: 'timers' }));

    textInputId += 1;

}



/** Search the filteredSpells array from showSuggestions function.
 * Return true if the input val is in the array somewhere. 
 */
function search(arr, targetId) {
    const searchText = $(`#${targetId}`).val()

    console.log(searchText)
    return arr.filter(element => element.toLowerCase().includes(searchText));
}

function searchHandler(e) {
    /** 
     * When keypress is registered, show suggestions from cachedSpells so user can choose if desired.
     * Use the target id to make sure correct input is being searched. 
     */
    const targetId = e.target.id
    showSuggestions(cachedSpells, targetId)
}

function showSuggestions(obj, targetId) {
    /* Show suggestions of spells based on letters input. */

    $('#spell-suggestions').empty(); //Start with a fresh slate for each keypress

    let spellNames = filterClass(obj);
    console.log(spellNames)
    let filteredSpells = search(spellNames, targetId);

    console.log(Object.keys(obj), obj)
    Object.keys(obj).forEach((key) => {
        const spell = obj[key];
        if (filteredSpells.includes(spell.name)) {
            console.log(spell.name)
            $('#spell-suggestions').append(`<li><img src=${spell.icon}>${spell.name}</li>`);
        }
    })
}


function useSuggestion(e) {
    /** Change the input val to the suggested spell text. */

    let suggestionText = e.target.innerText;

    if ($(e.target).is('img')) {
        suggestionText = $(e.target).closest('li').text(); //We want the user to be able to click the img or the text.
    }

    const inputElement = $(e.target).closest('.suggestions-box').find('input[type=text]');
    inputElement.val(suggestionText);

    $('#spell-suggestions').empty();
}

function newSuggestionsList() {
    $('.suggestions').empty();
}