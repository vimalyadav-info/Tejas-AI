$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    })


    //Siri configration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });


    //siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeOutUo",
        },
    })


    //micbutton click event
    $("#micbutton").click(function () {
        eel.playAssistantSound()
        $("#oval").attr("hidden", true);
        $("#siriwave").attr("hidden", false);
        eel.allCommands()()
    });



    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);



    // to play assisatnt 
    
    
    function PlayAssistant(message) {

        if (message != "") {

            $("#oval").attr("hidden", true);
            $("#siriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#micbutton").attr('hidden', false);
            $("#sendbutton").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#micbutton").attr('hidden', false);
            $("#sendbutton").attr('hidden', true);
        }
        else {
            $("#micbutton").attr('hidden', true);
            $("#sendbutton").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // send button event handler
    $("#sendbutton").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)

    });


    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });




});