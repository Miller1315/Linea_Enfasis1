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
    //factor <= 1 = 
    if(factor_servicio2 < 1 || factor_servicio2 >  3){
       alert("El factor de servicio debe estar entre 1 y 3")
       pResult.innerText = " " ;
    }

    }


let centrifugo_500 = document.querySelector("#centrifugo-500");
let centrifugo_750 = document.querySelector("#centrifugo-750");
let centrifugo_1000 = document.querySelector("#centrifugo-1000");
let absorcion_500 = document.querySelector("#absorcion-500");
let absorcion_750 = document.querySelector("#absorcion-750");
let absorcion_1000 = document.querySelector("#absorcion-1000");

let btn2 = document.querySelector('#btnCalcular2');
let pResult2 = document.querySelector('#result2');

//Casillas centrifugo y absorcion
let rp1 = document.querySelector('#rp1');
let g1 = document.querySelector('#g1');
let c1 = document.querySelector('#c1');
let o1 = document.querySelector('#o1');
let ft1 = document.querySelector('#ft1');
let e1 = document.querySelector('#e1');
let b1 = document.querySelector('#b1');


let g2 = document.querySelector('#g2');
let c2 = document.querySelector('#c2');
let o2 = document.querySelector('#o2');
let capex2 = document.querySelector('#capex2');
let b2 = document.querySelector('#b2');


function btnOnClick2() {

    let centrifugo_5002 = Number(centrifugo_500.value); //774  
    let centrifugo_7502 = Number(centrifugo_750.value);  //10
    let centrifugo_10002 = Number(centrifugo_1000.value); //5.5
    let absorcion_5002 =Number(absorcion_500.value)
    let absorcion_7502 =Number(absorcion_750.value)
    let absorcion_10002 =Number(absorcion_1000.value)
    
    totalc= (500*centrifugo_5002)+(750*centrifugo_7502)+(1000*centrifugo_10002)
    totala= (500*absorcion_5002)+(750*absorcion_7502)+(1000*absorcion_10002)
    totales = totala + totalc

    pResult2.innerText = "Resultado: " + totales;

    rrp1=totalc*0.3190995427365	
    rg1=(totalc*511.13199046407)/1000	
    rc1=(totalc*0.0035174111853)*(1925000/0.88)	
    ro1=rc1*0.03	
    	
    rcapex1=totalc*0.0035174111853
    rft1=rcapex1*1000000	
    re1=rcapex1*1700000	
    rb1=rcapex1*2000000

    //Absorción
    rg2=(totala*511.13199046407)/1000		
    rc2=((totala * 0.0035174111853)*(1925000/0.88))		
    ro2=rc2*0.03		
  		
    rcapex2=totala*0.0035174111853		
    rft2=(rcapex2*1000000)*1.015		
    rb2=rcapex2*2000000 	
    

    pResult2.innerText = "Resultado: " + totales;
    rp1.innerText = rrp1;
    g1.innerText = rg1;
    c1.innerText = rc1;
    o1.innerText = ro1;
    ft1.innerText = rft1;
    e1.innerText = re1;
    b1.innerText = rb1;

    g2.innerText = rg2;
    c2.innerText = rc2;
    o2.innerText = ro2;
    capex2.innerText = rcapex2;
    b2.innerText = rb2;


    
    }



    