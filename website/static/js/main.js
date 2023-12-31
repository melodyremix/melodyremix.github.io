const hoursEl= document.querySelector('#hours');
const minutesEl= document.querySelector('#minutes');
const secondsEl= document.querySelector('#seconds');
const btnStart = document.querySelector('.btn-start');
const btnPause = document.querySelector('.btn-pause');
const btnStop = document.querySelector('.btn-stop');
const btnReset = document.querySelector('.btn-reset');
let interval;
let pause= false;
let totalSeconds= 0;
let totalSecondsBackup=0;
var bell = new Audio('/static/bell.mp3');

init();

function init() {
    btnPause.getElementsByClassName.display='none';
    btnStop.getElementsByClassName.display='none';
    btnReset.getElementsByClassName.display='none';

    btnStart.addEventListener('click', () => {
        const hours= parseInt(hoursEl.value);
        const minutes= parseInt(minutesEl.value);
        const seconds= parseInt(secondsEl.value);
    
        console.log(hours, minutes, seconds);
    
        totalSecondsBackup = totalSeconds = hours * 60 * 60 + minutes*60 + seconds;

        if(totalSeconds <0){
            return;
        }
    
        startTimer(totalSeconds);

        btnPause.style.display= 'inline-block';
        btnStop.style.display= 'inline-block';
        btnReset.style.display= 'inline-block';
        btnStart.style.display='none';
    });

    btnPause.addEventListener('click', () =>{
        pause= !pause;
        if(pause){
            btnPause.innerText = 'Resume';
        }
        else{
            btnPause.innerText = 'Pause';
        }
    });

    btnStop.addEventListener('click', () =>{
        stopTimer();
        totalSeconds = totalSecondsBackup;
        pause = false;
        updateInputs();

        btnPause.style.display= 'none';
        btnStop.style.display= 'none';
        btnReset.style.display= 'none';
        btnStart.style.display='';
        
    });

    btnReset.addEventListener('click', () =>{
        totalSeconds = totalSecondsBackup;
        updateInputs();
        startTimer();

        btnPause.style.display= 'inline-block';
        btnStop.style.display= 'inline-block';
        btnReset.style.display= 'inline-block';
        btnStart.style.display='none';
    });
}


function startTimer() {
    interval= setInterval(() => {
        if(pause) return;
        totalSeconds--;
        updateInputs(totalSeconds);
        if(totalSeconds <=0){
            stopTimer();
            bell.play();
        }
    }, 1000);
}

function stopTimer() {
    interval = clearInterval(interval);
}


function updateInputs() {
    const hours = Math.floor(totalSeconds/60/60);
    const minutes= Math.floor(totalSeconds/60);
    const seconds= totalSeconds% 60;

    hoursEl.value= hours;
    minutesEl.value= minutes;
    secondsEl.value= seconds;

}
