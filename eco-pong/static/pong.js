var animate = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || function (callback) {
        window.setTimeout(callback, 1000 / 60)
    };
var canvas = document.createElement("canvas");
//canvas.style="background:url('https://www.w3schools.com/tags/img_the_scream.jpg')";
var width = 400;
var height = 500;
var player1Speed = Math.round((25 + $$player1Energy$$)/4);
var player2Speed = Math.round((25 + $$player2Energy$$)/4);
console.log("player 1 and 2 incoming");
console.log(player1Speed);
console.log(player2Speed);
var player1Score = 0;
var player2Score = 0;
var player1ID = "$$player1ID$$";
var player2ID = "$$player2ID$$";
canvas.width = width;
canvas.height = height;
var context = canvas.getContext('2d');
var player = new Player();
var computer = new Computer();
var ball = new Ball(width/2, height/2);

var keysDown = {};

var render = function () {
    img = document.createElement("img");
    img.src="http://helthelia.com/catalog/bk_slide/images/patterns_light_background_surface_texture_50722_1920x1080.jpg";
    context.drawImage(img,0,0);
    player.render();
    computer.render();
    ball.render();
};

var update = function () {
    player.update();
    computer.update(ball);
    ball.update(player.paddle, computer.paddle);
};

var step = function () {
    update();
    render();
    animate(step);
};

function Paddle(x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.x_speed = 0;
    this.y_speed = 0;
}

Paddle.prototype.render = function () {
    context.fillStyle = "#0000FF";
    context.fillRect(this.x, this.y, this.width, this.height);
};

Paddle.prototype.move = function (x, y) {
    this.x += x;
    this.y += y;
    this.x_speed = x;
    this.y_speed = y;
    if (this.x < 0) {
        this.x = 0;
        this.x_speed = 0;
    } else if (this.x + this.width > width) {
        this.x = width - this.width;
        this.x_speed = 0;
    }
};

function Computer() {
    pWidth = 50;
    pHeight = 10;
    this.paddle = new Paddle((width/2) - (pWidth/2), 10, pWidth, pHeight);
}

Computer.prototype.render = function () {
    this.paddle.render();
};

Computer.prototype.update = function () {
    for (var key in keysDown) {
        var value = Number(key);
        console.log(value);
        if (value == 65) {
            this.paddle.move(-1*player1Speed, 0);
        } else if (value == 68) {
            this.paddle.move(player1Speed, 0);
        } else {
            this.paddle.move(0, 0);
        }
    }
};

function Player() {
    pWidth = 50;
    pHeight = 10;
    this.paddle = new Paddle((width/2) - (pWidth/2), height-pHeight-10, pWidth, pHeight);
}

Player.prototype.render = function () {
    this.paddle.render();
};

Player.prototype.update = function () {
    for (var key in keysDown) {
        var value = Number(key);
        if (value == 37) {
            this.paddle.move(-1*player2Speed, 0);
        } else if (value == 39) {
            this.paddle.move(player2Speed, 0);
        } else {
            this.paddle.move(0, 0);
        }
    }
};

function Ball(x, y) {
    this.x = x;
    this.y = y;
    this.x_speed = getRandomInt(0,10)-5;
    if (getRandomInt(0,1) == 0) {
      this.y_speed = 3;
    } else {
      this.y_speed = -3;
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

Ball.prototype.render = function () {
    context.beginPath();
    context.arc(this.x, this.y, 5, 2 * Math.PI, false);
    context.fillStyle = "#000000";
    context.fill();
};

Ball.prototype.update = function (paddle1, paddle2) {
    this.x += this.x_speed;
    this.y += this.y_speed;
    var top_x = this.x - 5;
    var top_y = this.y - 5;
    var bottom_x = this.x + 5;
    var bottom_y = this.y + 5;

    if (this.x - 5 < 0) {
        this.x = 5;
        this.x_speed = -this.x_speed;
    } else if (this.x + 5 > width) {
        this.x = width-5;
        this.x_speed = -this.x_speed;
    }

    if (this.y < 0) {
        this.x_speed = getRandomInt(0,10)-5;
        this.y_speed = 3;
        this.x = width/2;
        this.y = height/2;
        player2Score += 1;
        document.getElementById("player2ss").innerHTML = player2Score;
        if (player2Score == 3) {
          window.location.href = "/gameOver?winner=" + player2ID + "&loser=" + player1ID;
        }
    }
    else if (this.y > height) {
        this.x_speed = getRandomInt(0,10)-5;//getRandomInt(0,6)-3;
        this.y_speed = -3;
        this.x = width/2;
        this.y = height/2;
        player1Score += 1;
        document.getElementById("player1ss").innerHTML = player1Score;
        if (player2Score == 3) {
          window.location.href = "/gameOver?winner=" + player1ID + "&loser=" + player2ID
        }
    }

    if (top_y > height/2) {
        if (top_y < (paddle1.y + paddle1.height) && bottom_y > paddle1.y && top_x < (paddle1.x + paddle1.width) && bottom_x > paddle1.x) {
            this.y_speed = -3;
            this.x_speed += (paddle1.x_speed / 2);
            this.y += this.y_speed;
        }
    } else {
        if (top_y < (paddle2.y + paddle2.height) && bottom_y > paddle2.y && top_x < (paddle2.x + paddle2.width) && bottom_x > paddle2.x) {
            this.y_speed = 3;
            this.x_speed += (paddle2.x_speed / 2);
            this.y += this.y_speed;
        }
    }
};

document.getElementById("game").appendChild(canvas);
animate(step);

window.addEventListener("keydown", function (event) {
    keysDown[event.keyCode] = true;
});

window.addEventListener("keyup", function (event) {
    delete keysDown[event.keyCode];
});
