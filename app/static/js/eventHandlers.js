$(document).on('click', 'button.add-btn', addSpellHandler) //Adds new text input and timer.
$(document).on('keyup', 'input.spells', searchHandler) //For search box suggestions.
$(document).on('click', 'ul', useSuggestion) //Update spell input with suggestion.
$(document).on('click', 'input.spells', newSuggestionsList) //Clear suggestions when clicking another spell input.
$(document).on('click', 'button.timer-btn', addTimerHandler)
$(document).on('click', function(e){
    if(!$(e.target).hasClass('spells')){
        $('#spell-suggestions').remove()

    }
})

$('input[type=radio]').on('click', function () {
    $(this).prev().attr('checked', true);
    
})
