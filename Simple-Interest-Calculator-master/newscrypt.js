function testcompute()
{
num1 = 3
num2 = 4;
rate = 10
var interest1 = num1 * num2 * rate /100;
document.getElementById("result2").innerHTML = interest1;
}



function slider_function()
{
  /*var slider = document.getElementById("rate2");-->
  var output = document.getElementById("rate_val");
  document.getElementById("rate_val").innerHTML = slider;*/
  var x = document.getElementById("rate2").value;
  document.getElementById("rate_val").innerHTML = x + "%";
}
