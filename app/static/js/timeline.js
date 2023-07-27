$(function () {
    if ($('body').is('.Timeline')) {
        $(document).on('click', '.spell', spellOpacity);
    };
});

function spellOpacity(e) {
    //If spell is selected, make others less visable in case there is overlap of spells.
    const target = $(e.target).closest('.spell')
    let spellClass = target.attr('class');
    spellClass = spellClass.replace('spell', '').trim();
    
    if(!target.hasClass('opacity')) {
        const spellTitle = $(this).find('h4').text()
        if(target.hasClass('flex-img')){
            $('.assignment-container').children().each(function() {
                const h4 = $(this).find('h4').text()
                if (h4 !== spellTitle) {
                    $(this).toggleClass('opacity');
                    console.log(this)
                } 
            })
            $('.lane').children().each(function () {
                if (!$(this).hasClass(`${spellTitle}`)) {
                    $(this).toggleClass('opacity');
                } 
            });
        } else {
            $('.lane').children().each(function () {
                if (!$(this).hasClass(`${spellClass}`)) {
                    $(this).toggleClass('opacity');
                } 
            });
            $('.assignment-container').children().each(function() {
                const h4 = $(this).find('h4').text()
                if (h4 !== spellClass) {
                    $(this).toggleClass('opacity');
                    console.log(this)
                } 
            });
        }      
    } else if (target.hasClass('opacity')) {
        if(target.hasClass('flex-img')) {
            const spellTitle = $(this).find('h4').text()
                target.toggleClass('opacity')
                $('.lane').children().each(function () {
                    if ($(this).hasClass(`${spellTitle}`)) {
                        $(this).toggleClass('opacity');
                    } 
                });
        } else {
            $('.lane').children().each(function () {
                if ($(this).hasClass(`${spellClass}`)) {
                    $(this).toggleClass('opacity');
                } 
            });
        
            $('.assignment-container').children().each(function() {
                const h4 = $(this).find('h4').text()
                const [playerName, spellName] = h4.split(' ');
                console.log([playerName, spellName])
                if (target.hasClass(`${playerName} ${spellName}`)) {
                    $(this).toggleClass('opacity');
                }  
            })
        }
    }
}  
  