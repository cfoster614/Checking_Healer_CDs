/* Can use the functions found in apiQuerying */


function addSpellHandler() {
    /** 
     * Create a new  text input to add another healer cd/timer. 
     * We want the user to input as many spells as they want.
     */
    $('.suggestions').empty(); //TODO: Make this universal to reduce code. Anytime a user clicks off of the suggestions.
    
    const newSpellInput = $('<input>', { type: 'text', class: 'spells center', name: 'spells', placeholder: 'Revival', autocomplete: 'off'}); 
    const newPlayerInput = $('<input>', { type: 'text', class: 'player-name', name: 'player-name', placeholder: 'Player Name'})
    const newTimerBtn = $('<button>', { type: "button", class: 'btn timer-btn', text: 'Add new time' });
    const newTimeInput = $('<div>', { class: 'timers-wrapper sub-grid' }).append($('<input>', { type: 'text', class: 'timers', name: '', placeholder: '00:10'}));
    const spellWrapDiv = $('<div>', { class: 'spell-wrapper' }).append(newSpellInput, newPlayerInput, newTimerBtn);
    const newDiv = $('<div>', { class: 'spell-input-box sub-static-container box' }).append($('<div>', { class: 'form-header'}), spellWrapDiv, newTimeInput);
    
    $('#spell-form').append(newDiv);
}

function addTimerHandler(e) {
    /**
     * Add a new timer input to the spell container. 
     * Max 9.
     * If user clicks add timer before a spell is selected, recieve an error.
     * If a user could move on before selecting a spell, it will break the 'names'. The names should include the spell's name for easier sorting in the backend.
     */
    const spellNames = getSpellNames();
    const inputBox = $(e.target).closest('.spell-input-box');
    const container = inputBox.find('.timers-wrapper');
    const value = $(e.target).siblings('.spells')
    let inputVal = value.val();
    
    
        //Create new timer inputs.
        const newInput = $('<input>', { type: 'text', class: 'timers', name: `${inputVal}-timers`, placeholder: '00:10'});
        inputBox.find('.timers-wrapper').append(newInput); 
        inputBox.find('.timers').attr('name', `${inputVal}-timers`) 
        /**Change the previous inputs to the new spell for the 'name'.
         *This way we can group the timers by spell in the backend.
         */

    
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
    $('#spell-suggestions').remove();
    const target = e.target;
    const spellInputBox = $(target).closest('.spell-input-box');
    spellInputBox.append($('<ul>', { id: 'spell-suggestions', class: 'suggestions' }));

    if ($(spellInputBox).hasClass('max-height')) {
        $('#spell-suggestions').addClass('max-height');

    } 
    
    showSuggestions(cachedSpells, target);
}


function showSuggestions(obj, target) {
    /* Show suggestions of spells based on letters input. */
    
    let spellNames = filterClass(obj);
    let filteredSpells = search(spellNames, target);

    for (spell of cachedSpells) {
        if (filteredSpells.includes(spell.name)) {
            $('.suggestions').append(`<li data-index-number=${spell.id}, class="sub-flex box"><img src=${spell.icon}>${spell.name}</li>`);
           
        }
    }
}

function useSuggestion(e) {
    /** Change the input val to the suggested spell text. */
    const target = e.target;
    let suggestionText = $(target).text();
    const spellInputBox = $(target).closest('.spell-input-box');
    const inputElement = spellInputBox.find('.spells');
    const timers = spellInputBox.find('.timers');
    const header = spellInputBox.find('.form-header');
    const headerText = $(target).closest('.form-header').find('h4').text();
    const spellNames = getSpellNames();

    header.empty();
    header.addClass('flex-img title-box')
    if (suggestionText.indexOf(spellNames)) {

        if ($(target).is('img')) { //We want the user to be able to click the img or the text.
            suggestionText = $(target).closest('li').text(); 
            header.append($('<img>', { src: $(target).attr('src')}));
        } else {
            if (header.children().length === 0 || headerText !== suggestionText) {
                const img = $(target).find('img');
                header.append($('<img>', { src: `${img.attr('src')}`}));
                spellInputBox.addClass('max-height');
            }
        } 
        inputElement.val(suggestionText);
        timers.attr('name', `${suggestionText}-timers`); //Change timer input to match spell name put in.
    }
    $('#spell-suggestions').empty(); //Clear suggestions after clicking suggestion.
}


function newSuggestionsList() {
    $('.suggestions').empty(); //To ensure no suggestions are shown when clicking a new input.
}








