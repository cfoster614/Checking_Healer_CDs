$(document).on('click', 'button.add-btn', addSpellHandler) //Adds new text input and timer.
$(document).on('keyup', 'input.spells', searchHandler) //For search box suggestions.
$(document).on('click', 'ul', useSuggestion) //Update spell input with suggestion.
$(document).on('click', 'input.spells', newSuggestionsList) //Clear suggestions when clicking another spell input.
$(document).on('click', 'button.timer-btn', addTimerHandler)


$('input[type=radio]').on('click', function () {
    $(this).prev().attr('checked', true);
    
})


$('span').on('click', function(e){
    const id = $(this).data('id')
    console.log(id)

})


