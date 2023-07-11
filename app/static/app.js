/* Can use the functions found in apiQuerying */


function addSpellHandler() {
    /** 
     * Create a new  text input to add another healer cd/timer. 
     * We want the user to input as many spells as they want.
     */
    $('.suggestions').empty(); //TODO: Make this universal to reduce code. Anytime a user clicks off of the suggestions.
    
    const newSpellInput = $('<input>', { type: 'text', class: 'spells', name: 'spells', placeholder: 'Revival' }); 
    const newTimerBtn = $('<button>', { type: "button", class: 'btn timer-btn', text: 'Add new time' });

    const ulDiv = $('<div>', { class: 'suggestions-box' }).append($('<ul>', { id: 'spell-suggestions', class: 'suggestions' }));
    const spellWrapDiv = $('<div>', { class: 'spell-wrapper flex' }).append(newSpellInput, newTimerBtn)

    const newDiv = $('<div>', { class: 'spell-input-box' }).append($('<div>', { class: 'form-header flex' }), spellWrapDiv, $('<div>', { class: 'timers-wrapper' }), ulDiv)


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
    
    if (!inputVal) {
        alert('Add a spell name first.');

    } else if (container.children().length < 9) {
        const header = inputBox.find('.form-header');
        const h4 = header.find('h4');
        const ul = inputBox.find('.suggestions-box'); //Find closest ul.
        const li = $(ul).find('li:first-child'); //Since suggestions will show up, retrieve first li.
        const img = $(li).find('img'); //Get the spell image for the image source. Used to update the spell header box.
        const src = img.attr('src');

        if (spellNames.indexOf(inputVal) === -1) { 
            //Check if input value is in array of spell names.
            //If someone inserted 'rev', 'revival' should be the new text value.
            value.val(li.text())
        }

        if (header.children().length === 0 || $(h4).text() !== inputVal) {
            //We want the header to contain the correct spell name, and the correct image.
            //This will change the header if it's empty, or if the text of the header does not match the current input spell.
            header.empty();
            header.append($('<img>', { src: `${src}` }));
            header.append($('<h4>', { text: value.val()}));
        }

        //Create new timer inputs.
        const newInput = $('<input>', { type: 'text', class: 'timers', name: `${inputVal}-timers`, placeholder: '00:10'});
        $(e.target).closest('.spell-input-box').find('.timers-wrapper').append(newInput); 
        $(e.target).closest('.spell-input-box').find('.timers').attr('name', `${inputVal}-timers`) /**Change the previous inputs to the new spell for the 'name'.
                                                                                                    *This way we can group the timers by spell in the backend.
                                                                                                    */
        
    } else {
        container.off('click', addTimerHandler); //Turn off the ability to add more timers.
        alert('Maximum number of timers allowed.') /**Currently I only want to allow 9 input timers so it's not cluttered. 
                                                    *I don't think there are many cases where someone will want to check more than that anyway.
                                                    */

        //TODO: Do something other than an alert to prevent the user from create more timers.

    }
    $('.suggestions').empty(); 
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


    for (spell of cachedSpells) {
        if (filteredSpells.includes(spell.name)) {
            $('.suggestions').append(`<li data-index-number=${spell.id}><img src=${spell.icon}>${spell.name}</li>`);
        }
    }

}





function useSuggestion(e) {
    /** Change the input val to the suggested spell text. */

    let suggestionText = e.target.innerText;
    let suggestionValue = $(e.target).attr('data-index-number');
    const inputElement = $(e.target).closest('.spell-input-box').find('.spells');
    const hiddenInput = $(e.target).closest('.spell-input-box').find('.hidden-ids');
    const headerText = $(e.target).closest('.form-header').find('h4').text();
    const header = $(e.target).closest('.spell-input-box').find('.form-header');




    if ($(e.target).is('img')) {
        suggestionText = $(e.target).closest('li').text(); //We want the user to be able to click the img or the text.
        suggestionValue = $(e.target).closest('li').attr('data-index-number');
        console.log(suggestionValue)
    }

    inputElement.val(suggestionText);
    hiddenInput.val(suggestionValue);


    for (spell of cachedSpells) {
        if (spell.name === suggestionText) {
            if (header.children().length === 0 || headerText !== suggestionText) {
                header.empty();
                header.append($('<img>', { src: spell.icon }));
                header.append($('<h4>', { text: spell.name }));
                break;

            }
        }
    }
    $('#spell-suggestions').empty(); //Clear suggestions after clicking suggesion.
}


function newSuggestionsList() {
    $('.suggestions').empty(); //To ensure no suggestions are shown when clicking a new input.
}






