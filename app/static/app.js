/* Can use the functions found in apiQuery */

function addSpellHandler() {
    /** 
     * Create a new  text input to add another healer cd/timer. 
     */
    $('.suggestions').empty();

    const newUl = ($('<ul>', { id: 'spell-suggestions', class: 'suggestions' }));
    const ulDiv = $($('<div>', { class: 'suggestions-box' }));
    const newDiv = ($('<div>', { class: 'spell-input-box' }));
    const newSpellInput = ($('<input>', { type: 'text', class: 'spells', name: 'spells', placeholder: 'Revival' }));
    const newTimerInput = ($('<input>', { type: 'text', class: 'timers', placeholder: '00:10' }));

    ulDiv.append(newUl);
    newDiv.append(newSpellInput, newTimerInput, ulDiv);
    newDiv.insertBefore($('.add-btn'));
}

function search(arr, target) {
    /** Search the filteredSpells array from showSuggestions function.
     * Return true if the input val is in the array somewhere. 
     */
    const searchText = target.value;
    return arr.filter(element => element.toLowerCase().includes(searchText));
}


function searchHandler(e) {
    /** 
     * When keypress is registered, show suggestions from cachedSpells so user can choose if desired.
     * Use the target id to make sure correct input is being searched. 
     */
    const target = e.target;
    showSuggestions(cachedSpells, target);
}


function showSuggestions(obj, target) {
    /* Show suggestions of spells based on letters input. */

    $('.suggestions').empty(); //Start with a fresh slate for each keypress

    let spellNames = filterClass(obj);
    let filteredSpells = search(spellNames, target);

    console.log(Object.keys(obj), obj)
    Object.keys(obj).forEach((key) => {
        const spell = obj[key];
        if (filteredSpells.includes(spell.name)) {
            $('.suggestions').append(`<li><img src=${spell.icon}>${spell.name}</li>`);
        }
    })
}


function useSuggestion(e) {
    /** Change the input val to the suggested spell text. */

    let suggestionText = e.target.innerText;

    if ($(e.target).is('img')) {
        suggestionText = $(e.target).closest('li').text(); //We want the user to be able to click the img or the text.
    }

    const inputElement = $(e.target).closest('.spell-input-box').find('.spells');
    inputElement.val(suggestionText);

    $('#spell-suggestions').empty(); //Clear suggestions after clicking suggesion.
}


function newSuggestionsList() {
    $('.suggestions').empty(); //To ensure no suggestions are shown when clicking a new input.
}






