// Message timeout

setTimeout(function () {
    var messages = document.getElementById('msg');
    console.log(`Message Elem: ${messages}`);
    var alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);


// Change colour scheme to high contrast

var highContrastBlue = '#164aa6';
var highContrastRed = '#ab2237';
var highContrastMute = '#000000';

var logoblue = ' #3186e0';
var logored = ' #eb7575';
var mute = ' darkgrey';

// Get the root element
var r = document.querySelector(':root');


function toggleContrast() {
    var rs = getComputedStyle(r);
    var current_blue = rs.getPropertyValue('--logoblue');

    if (current_blue == logoblue) {
        r.style.setProperty('--logoblue', highContrastBlue);
        r.style.setProperty('--logored', highContrastRed);
        r.style.setProperty('--mute', highContrastMute);

        localStorage.setItem('current_blue', highContrastBlue);
        localStorage.setItem('current_red', highContrastRed);
        localStorage.setItem('current_mute', highContrastMute);
    }
    else {
        r.style.setProperty('--logoblue', logoblue);
        r.style.setProperty('--logored', logored);
        r.style.setProperty('--mute', mute);

        localStorage.setItem('current_blue', logoblue);
        localStorage.setItem('current_red', logored);
        localStorage.setItem('current_mute', mute);
    }
}

function maintainContrast() {
    var current_blue = localStorage.getItem('current_blue');
    var current_red = localStorage.getItem('current_red');
    var current_mute = localStorage.getItem('current_mute');

    r.style.setProperty('--logoblue', current_blue);
    r.style.setProperty('--logored', current_red);
    r.style.setProperty('--mute', current_mute);
}
