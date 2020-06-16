let canvas = document.getElementById("snake");
let context = canvas.getContext("2d");
let box = 32;
let snake = [];
snake[0] = {
  x: 8*box,
  y: 8*box
}

function criarBG() {
  context.fillStyle = "lightgreen";
  context.fillRect(0,0,16 * box, 16 * box);
}


function makeSnake() {
  for(i=0; i<snake.lenght; i++) {
    context.fillStyle = "green";
    context.fillRect(snake[1].x, snake[1].y, box, box);
  }
}

criarBG();
makeSnake();