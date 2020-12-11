$( document ).ready(function() {
    initLoginButton();
});

function initLoginButton(){
    $('#login-button').on('click', function(){
        console.log("buttoon clicked");
    })
}