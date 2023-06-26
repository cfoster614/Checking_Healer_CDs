$('input[type=radio]').on('click', function() {
    $(this).prev().attr('checked', true);
    console.log(this);
})

$('.add-btn').on('click', function() {
    const newSpellInput = ($('<input>', {type: 'text', class:'spells'}));
    const newTimerInput = ($('<input>', {type: 'text', class:'timers'}));
    $('#spell-form input.spells').each(function() {
        newSpellInput.insertAfter($(this));
    })

    $('#timer-form input.timers').each(function() {
        newTimerInput.insertAfter($(this));
    })
})