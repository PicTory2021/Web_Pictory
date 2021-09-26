
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
    submitName = document.getElementById('submit')

    console.log(submitName);

    function onSubmit() {
        const inputName = document.querySelector(".username");
        const name = inputName.value;
        localStorage.setItem("username", name);
        console.log(localStorage.getItem("username"));
        window.location.href="/main/"
    }

    submitName.addEventListener("click", onSubmit);
}
