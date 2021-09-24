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

