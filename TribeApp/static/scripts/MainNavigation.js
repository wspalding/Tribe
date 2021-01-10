$( document ).ready(function() {
    initLoginModal();
    initLoginForm();
    initSignUpForm();
});

function initLoginModal(){
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

function initLoginForm() {
    $('#login-form').on('click', function(event){
    }) 
}

function initSignUpForm() {
    $('#signup-submit-feild').submit(function(event){
        var email = $('#signup-email-feild').val()
        var username = $('#signup-username-feild').val()
        var password = $('#signup-password-feild').val()
        console.log(email, username, password)
        signup(email, username, password)
    })
}


function login()
{
    
}

function logout()
{

}

function signup(email, username, password)
{
    $.post('/auth/signup', {
        email: email,
        username: username,
        password: password
    })
    .done(function(response) {
        console.log(response)
    })
    .fail(function(error) {
        console.log(error)
    })
}