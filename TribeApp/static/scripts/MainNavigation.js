$( document ).ready(function() {
    initLoginButton();
});

function initLoginButton(){
    $('#login-button').on('click', function(event){
        $('#login-modal').css('display', 'block');
    })
    // When the user clicks anywhere outside of the modal, close it
    $(window).on('click', function(event) {
        if (event.target == $('#login-modal')[0]) {
            $('#login-modal').css('display', 'none');
        }
    })
}