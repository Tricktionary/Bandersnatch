function showSpinner(button){
    var $spinner = '<div class="ui active tiny inline loader"></div>';
    var $buttonContents = button.html();
    button.addClass('button-disabled');
    button.html($spinner);

    return $buttonContents
}

function hideSpinner($button, $buttonContents) {
    $button.removeClass('button-disabled');
    $button.html($buttonContents);
    $button.prop('disabled', false);
}