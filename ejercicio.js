const conts1=1000
const conts2=0.0003069      
let factor_servicio = document.querySelector("#factor-servicio");   
let caudal = document.querySelector("#caudal");
let temp_e = document.querySelector("#tentrada");
let temp_s = document.querySelector("#tsalida");

let btn = document.querySelector('#btnCalcular');
let pResult = document.querySelector('#result');


function btnOnClick() {

    let caudal2 = Number(caudal.value); //774  
    let temp_e2 = Number(temp_e.value);  //10
    let temp_s2 = Number(temp_s.value); //5.5
    let factor_servicio2 =Number(factor_servicio.value)
    

    const sumaInputs= caudal2*(temp_e2-temp_s2)*factor_servicio2*conts1*conts2

    pResult.innerText = "Resultado: " + sumaInputs;
    }


    let centrifugo_500 = document.querySelector("#centrifugo-500");
let centrifugo_750 = document.querySelector("#centrifugo-750");
let centrifugo_1000 = document.querySelector("#centrifugo-1000");
let absorcion_500 = document.querySelector("#absorcion-500");
let absorcion_750 = document.querySelector("#absorcion-750");
let absorcion_1000 = document.querySelector("#absorcion-1000");