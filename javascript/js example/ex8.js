function clock(){
var monthName=["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
    var dayNames=["Sunday","Monday"," Tuesday"," Wednesday","Thursday","Friday"," Saturday"];
    var today =new Date();
    document.getElementById('Date').innerHTML=(dayNames[today.getDay()]+""+
    today.getDate()+''+ monthName[today.getMonth()]+''+today.getFullYear());
    var h= today.getHours();
    var m= today.getMinutes();
    var s= today.getSeconds();
    var day =h<11 ? 'AM': 'PM';
    h=h<10? '0'+h: h;
    m=m<10? '0'+m: m;
    s=s<10? '0'+s: s;
    document.getElementById("hour").innerHTML = h;
    document.getElementById("min").innerHTML =m;
    document.getElementById("sec").innerHTML =s;

}var inter = setInterval(clock,1000);