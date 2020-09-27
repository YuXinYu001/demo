function printHello()
{
    //document.getElementById("demo").innerHTML="hello";
    //window.alert("hello js");
    //document.write("hello js");
    var day = document.getElementById("time").value;
    var sTime = day + " 00:00:00"
    var eTime = day + " 23:59:59"
    console.log(sTime,"-", eTime);
}
