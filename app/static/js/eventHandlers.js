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

$('.btn.delete').on('click', function() {
    $('#spell-form').remove();
    $('#spell-selection').append($('<div>', {id: 'spell-form', class: 'main-grid'}))
})

$('input[type=radio]').on('click', function () {
    $(this).prev().attr('checked', true);
    
})

$(document).on('click', '.final-btn', function() {
    //Change the name of each input to be more specific so that the backend can group it all together.
    $('#spell-form').children('.spell-input-box').each(function(){
        const playerNameInput = $(this).find('.player-name');
        const playerName = playerNameInput.val()
        console.log(playerName)
        const spellInput = $(this).find('.spells')

        spellInput.attr('name', `spells ${playerName}`)
        
    
        // playerNameInput.attr('name', `${spellInput}-${playerName}`);
        
        $('.timers-wrapper').children('.timers').each(function(){
            $(this).find('.timers').attr('name', `${spellInput} ${playerName} timers`)
        })
    })
})