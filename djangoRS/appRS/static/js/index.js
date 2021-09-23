$("document").ready(function() {
    var app = document.getElementById('app');

    var typewriter = new Typewriter(app, {
        loop: true
    });

    typewriter.typeString('World!')
        .pauseFor(2500)
        .deleteAll()
        .typeString('Strings')
        .pauseFor(2500)
        .deleteChars(7)
        .typeString('<strong>altered!</strong>')
        .pauseFor(2500)
        .start();
})