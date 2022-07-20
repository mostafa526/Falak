var first = document.getElementById("berv");
var second = document.getElementById("fees");
var third = document.getElementById("cradit");
var forth = document.getElementById("t");

var costt = document.getElementById("cost");
var taxx = document.getElementById("tax");
var noww = document.getElementById("now");
var lastt = document.getElementById("last");

var totall = document.getElementById("total");


var datte = document.getElementById("date");
var ressDate = document.getElementById("resDate");

var cur;

function My_Date() {
    cur= document.getElementById("date").value;
ressDate.innerHTML=cur;
   

}

function Sum() {
    return (parseInt(first.value) + parseInt(second.value) + parseInt(third.value) + parseInt(forth.value));
}
document.addEventListener("keyup", calcTotal);
function calcTotal() {
    if (first.value.length != 0 && second.value.length != 0 && third.value.length != 0 && forth.value.length != 0) {
        totall.innerText =  Sum() ;
        totall.style.display = "inline";
        totall.style.color="brown";
    }
    else {

        totall.style.display = "none";
    }

}

document.addEventListener("keyup", displayFirst);
function displayFirst() {
    if (first.value.length != 0 ) {
        costt.innerText =  first.value ;
        costt.style.display = "inline";
    }
    else {

        costt.style.display = "none";
    }

}
document.addEventListener("keyup", displaySecond);
function displaySecond() {
    if (second.value.length != 0 ) {
        taxx.innerText =  second.value ;
        taxx.style.display = "inline";
    }
    else {

        taxx.style.display = "none";
    }

}
document.addEventListener("keyup", displayThird);
function displayThird() {
    if (third.value.length != 0 ) {
        noww.innerText =  third.value ;
        noww.style.display = "inline";
    }
    else {

        noww.style.display = "none";
    }

}

document.addEventListener("keyup", displayForth);
function displayForth() {
    if (forth.value.length != 0 ) {
        lastt.innerText =  forth.value ;
        lastt.style.display = "inline";
    }
    else {

        lastt.style.display = "none";
    }

}



var moshtarekNumm =document.getElementById("moshtarekNum");
var totalBakaa = document.getElementById("totalBaka");
var totalBakaa2 = document.getElementById("totalBaka2");


var totalbaka3 = document.getElementById("totalBaka3");

function check(){
    var selected = document.getElementById("selectBaka").value;
    if(selected=="fadya"){
        var res = parseInt(moshtarekNumm.value)*250;
        totalBakaa.innerHTML=res;
        var totalres= res + (100* parseInt(moshtarekNumm.value)  );
        totalBakaa2.innerHTML=totalres;
        var res = parseInt(moshtarekNumm.value)*250*3;
        totalbaka3.innerHTML=res;
    }
    else if(selected=="blatinia"){
        var res2 =  parseInt(moshtarekNumm.value)*1000;
        totalBakaa.innerHTML=res2;
        var totalres2=res2 + (250 * parseInt(moshtarekNumm.value) );
        totalBakaa2.innerHTML= totalres2;
        var res2 =  parseInt(moshtarekNumm.value)*1000*3;
        totalbaka3.innerHTML=res2;
    }
    else if(selected=="zahabia"){
        var res3 =  parseInt(moshtarekNumm.value)*500;
        totalBakaa.innerHTML=res3;
        var totalres3=res3 + (100 * parseInt(moshtarekNumm.value) );
        totalBakaa2.innerHTML= totalres3;
        var res3 =  parseInt(moshtarekNumm.value)*500*3;
        totalbaka3.innerHTML=res3;

    }
    else if(selected=="basic"){
        var res4 =  parseInt(moshtarekNumm.value)*100;
        totalBakaa.innerHTML=res4;
        var totalres4=res4 + (100 * parseInt(moshtarekNumm.value) );
        totalBakaa2.innerHTML= totalres4;
        var res4 =  parseInt(moshtarekNumm.value)*100*3;
        totalbaka3.innerHTML=res4;

    }
}




var datte2 = document.getElementById("dateT");
var ressDate2 = document.getElementById("resDateT");

var curDate;

function My_DateT() {
   curDate= document.getElementById("dateT").value;
ressDate2.innerHTML=curDate;
   

}


function savee () {
 const sav=this.document.getElementById("save");


  html2pdf().from(sav).save();
}


function saveeT () {
 const sav=this.document.getElementById("saveT");


  html2pdf().from(sav).save();
}
 