$( document ).ready(function() {
    initLoginButton();
});

function initLoginButton(){
    $('#login-button').on('click', function(event){
        $('#login-modal').style.display = "block";
    })
    // When the user clicks anywhere outside of the modal, close it
    $(window).on('click', function(event) {
        if (event.target == $('#login-button')) {
            $('#login-modal').style.display = "none";
        }
    })
}