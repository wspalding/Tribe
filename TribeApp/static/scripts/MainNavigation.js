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
    $('#login-form').on('submit', function(event){
        var username = $('#login-username-field').val();
        var password = $('#login-password-field').val();
        var remember_me = $('#login-remember-me-field').val();
        login(username, password, remember_me);
        return false;
    }) 
}

function initSignUpForm() {
    $('#signup-form').on('submit', function(event){
        var email = $('#signup-email-feild').val();
        var username = $('#signup-username-feild').val();
        var password = $('#signup-password-feild').val();
        signup(email, username, password);
        return false;
    })
}


function login(username, password, remember_me)
{
    $.ajax({
        type: 'POST',
        url: '/auth/login', 
        contentType: 'application/json',
        data : JSON.stringify({
            remember_me: remember_me,
            username: username,
            password: password
        })
    })
    .done(function(response) {
        if(response.success)
        {
            console.log('success')
        }
        console.log(response)
    })
    .fail(function(error) {
        console.log(error)
    })
}

function logout()
{

}

function signup(email, username, password)
{
    $.ajax({
        type: 'POST',
        url: '/auth/signup', 
        contentType: 'application/json',
        data : JSON.stringify({
            email: email,
            username: username,
            password: password
        })
    })
    .done(function(response) {
        console.log(response)
    })
    .fail(function(error) {
        console.log(error)
    })
}