$(document).ready(function () {
    $('#autocomplete').autocomplete({
        serviceUrl: '/supporter/autocomplete',
        contentType: 'application/json',
        dataType: 'json',
        onSelect: function (suggestion) {
            document.cookie = "supporter=" + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
            document.cookie = "supporter=" + suggestion.data;
            $('#su_value').val(suggestion.data);
        }
    });
    $('#su_chosen').chosen();
});