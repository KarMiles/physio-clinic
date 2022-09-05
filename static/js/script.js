// Message timeout

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);


// Change font colours to high contrast

var highContrastBlue = '#164aa6';
var highContrastRed = '#ab2237';

var logoblue = ' #3186e0';
var logored = ' #eb7575';

// Get the root element
var r = document.querySelector(':root');


function toggleContrast() {
    var rs = getComputedStyle(r);
    var current_blue = rs.getPropertyValue('--logoblue');
    // var current_red = rs.getPropertyValue('--logored');

    if (current_blue == logoblue) {
        r.style.setProperty('--logoblue', highContrastBlue);
        r.style.setProperty('--logored', highContrastRed);

        localStorage.setItem('current_blue', highContrastBlue);
        localStorage.setItem('current_red', highContrastRed);

        // localStorage.setItem('current_blue', highContrastBlue);
        // localStorage.setItem('current_red', highContrastRed);
    }
    else {
        r.style.setProperty('--logoblue', logoblue);
        r.style.setProperty('--logored', logored);

        localStorage.setItem('current_blue', logoblue);
        localStorage.setItem('current_red', logored);
    };
}

function contrastFunction_maintain() {
    let current_blue = localStorage.getItem('current_blue');
    let current_red = localStorage.getItem('current_red');

    r.style.setProperty('--logoblue', current_blue);
    r.style.setProperty('--logored', current_red);
}
