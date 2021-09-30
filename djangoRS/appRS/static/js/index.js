
$("document").ready(function() {
    var app = document.getElementById('app');

    var typewriter = new Typewriter(app, {
        loop: true
    });

    typewriter.typeString('Pic')
        .pauseFor(700)
        .typeString('Tory.')
        .pauseFor(10000)
        .start();
})




window.onload = function() {

    const savedUsername = localStorage.getItem("username");
    const inputNameBox = document.querySelector("#noUsername");
    let inputName = (document.querySelector(".username"));
    const greeting = document.querySelector("#yesUsername h3");
    const loginForm = document.querySelector("#login-form");

    if(savedUsername !== null && savedUsername !== ""){ //username이 있을 때
        $(inputNameBox).hide();
        greeting.innerHTML = `${savedUsername}님, 반갑습니다.`;
        inputName.value = savedUsername;
    } else{
        loginForm.addEventListener("submit",onLoginSubmit);
    }

    function onLoginSubmit(){
        inputName = inputName.value;
        localStorage.setItem("username", inputName);
    }
}
