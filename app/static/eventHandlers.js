$(document).on('click', 'button.add-btn', addSpellHandler) //Adds new text input and timer.
$(document).on('keyup', 'input.spells', searchHandler) //For search box suggestions.
$(document).on('click', 'ul', useSuggestion) //Update spell input with suggestion.
$(document).on('click', 'input.spells', newSuggestionsList) //Clear suggestions when clicking another spell input.

$('input[type=radio]').on('click', function () {
    $(this).prev().attr('checked', true);
})

