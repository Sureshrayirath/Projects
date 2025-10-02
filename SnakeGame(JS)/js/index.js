let direction = {x: 0, y: 0};
const foodSound = new Audio('eat.wav');
const gameOverSound = new Audio('end.wav');
const moveSound = new Audio('turn.wav');
let speed = 2;
let lastPaintTime = 0;
let snakeArr = [
    {x: 13,y:15}
]
food = {x: 13,y:15};

function main(ctime)
{
    window.requestAnimationFrame(main);
    console.log(ctime)
    if((ctime - lastPaintTime)/1000 < 1/speed)
    {
        return;
    }
    lastPaintTime = ctime;
    gameEngine();
}
function gameEngine()
{
    //Updating Snake array & Food

    //Display the snake & Food
    BeforeUnloadEvent.innerHTML = "";
    snakeArr.forEach((e, index)=>{
        snakeElement = document.createElement('div');
        snakeElement.style.gridRowStart = e.y;
        snakeElement.style.gridColumnStart = e.x;
        snakeElement.classList.add('food')
        BeforeUnloadEvent.appendChild(snakeElement);
    });


}