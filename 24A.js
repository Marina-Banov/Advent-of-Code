class Tile {
    constructor(q, r, offset) {
        this.q = q;
        this.r = r;
        this.flipped = false;
        this.id = r*mapRadius*2 + q + offset;
        this.points = [];
        for (var i = 0; i < 6; i++) {
            this.points.push(this.hexCorner(i));
        }
    }

    center() {
        var x = (sqrt(3) * this.q + sqrt(3)/2 * this.r) * hexSize;
        var y = (0 * this.q + 3/2 * this.r) * hexSize;
        return createVector(x + width/2, y + height/2);
    }

    hexCorner(i) {
        var center = this.center();
        var angleDeg = 60 * i + 30;
        var angleRad = PI/180 * angleDeg;
        return createVector(center.x + hexSize * cos(angleRad), center.y + hexSize * sin(angleRad));
    }
}

var hexSize = 10;
var mapRadius = 17;
var tiles = [];
var stop = mapRadius*mapRadius*2 + mapRadius;

function setup() { 
    createCanvas(700, 550);
    angleMode(RADIANS);
    for (var r = 0; r < mapRadius * 2; r++) {
        var rOffset = floor(r/2);
        for (var q = -rOffset; q < (mapRadius*2) - rOffset; q++) {
            tiles.push(new Tile(q, r, rOffset));
        }
    }
} 

function draw() { 
    background(255);
    stroke(0);
    strokeWeight(1);
    translate(-width/2 + 30, -height/2 + 30);
    for (var t of tiles) {
        drawHexagon(t);
    }
}

function drawHexagon(tile) {
    if (tile.id == stop) {
        fill(255, 150, 150);
    } else {
        fill(tile.flipped ? 0 : 255);
    }
    beginShape();
    for (i = 1; i <= 6; i++) {
        vertex(tile.points[i % 6].x, tile.points[i % 6].y);
        line(tile.points[i-1].x, tile.points[i-1].y, tile.points[i % 6].x, tile.points[i % 6].y);
    }
    endShape();
}

function move(step) {
    stop += step + (((step < -1 || step > 1) && tiles[stop].r % 2 == 1) ? 1 : 0);
}

function flip() {
    tiles[stop].flipped = !tiles[stop].flipped;
    res.innerHTML = tiles.filter(t => t.flipped).length;
}

function home() {
    stop = mapRadius*mapRadius*2 + mapRadius;
}

function reset() {
    tiles.forEach(t => t.flipped = false);
    res.innerHTML = 0;
}

function read() {
    steps.value.split(/\r?\n/).forEach(s => {
        home();
        var position = 0;
        while (position < s.length) {
            switch (s[position]) {
                case 'e':
                    move(1);
                    break;
                case 'w':
                    move(-1);
                    break;
                case 'n':
                    move(-2*mapRadius - ((s[position+1] == 'w') ? 1 : 0));
                    position++;
                    break;
                case 's':
                    move(2*mapRadius - ((s[position+1] == 'w') ? 1 : 0));
                    position++;
                    break;
            }
            position++;
        }
        flip();
    });
    home();
}
