$(document).ready(function () {

    //display speak message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

    //Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#oval").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }


    eel.expose(senderText)
    function senderText(message) {
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatbox.innerHTML += `<div class="row justify-content-end wb-4">
                <div class="width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`;
    
            // Scroll to the bottom of the chat box
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }
    
    eel.expose(receiverText)
    function receiverText(message) {
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatbox.innerHTML += `<div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="receiver_message">${message}</div>
                </div>
            </div>`;
    
            // Scroll to the bottom of the chat box
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }


});