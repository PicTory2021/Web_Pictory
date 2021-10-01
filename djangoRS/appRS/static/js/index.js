
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

const images=[
    '고창읍성1.png',
    '안성팜랜드1.jpg',
    '과학동아천문대1.png',
    '흔들전망대1.jpg',
    '후정해수욕장1.jpg',
    '가산수피아1.JPG',
]
let index = 0;

function changeBanner(){
    const banner = document.querySelector("#banner");
    console.log(images[index]);
    banner.style.backgroundImage = `url("/static/images/overlay.png"), url("/static/tour_img/${images[index]}")`
    index++;
    if(index == images.length){
        index=0;
    }
}

setInterval(changeBanner, 5000);