let s = 0;
let w = 0;
let h = 0;
let a = 255;

function setup() {
    createCanvas(windowWidth, windowHeight-5);
    w = windowWidth;
    h = windowHeight;
}

function draw() {
    background(255);

    // Debug :
    textSize(32);
    fill(50);
    text(s, w/2, h/2);

    switch(s)
    {
        case 0:
            var message = "help"
        break;
    }

    // Draw final text
    fill(50,50,50,a);
    text(message, w/2 - message.length*8, h/1.5);
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight-5);
    w = windowWidth;
    h = windowHeight;
}

function mousePressed() {s++}