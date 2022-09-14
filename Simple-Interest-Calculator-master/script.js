function compute()
{
    p = document.getElementById("principal").value;


       var principal = document.getElementById("principal").value;

       if (principal <= 0) {
           alert("Enter a positive number");
       }

       var rate = document.getElementById("rate2").value;
       var years = document.getElementById("years").value;
       var interest = principal * years * rate /100;
       var year = new Date().getFullYear()+parseInt(years);
       function updateRate()
{
    var rateval = document.getElementById("rate2").value;
    document.getElementById("rate_val").innerText=rateval;

}
     document.getElementById("result2").innerHTML = "If you deposit " + principal + "," +
     "<br> at an interest rate of " + rate + "%" + "," +
     "<br> You will receive an amount of " + interest + "," +
     "<br> in the year " + (year)

;
}


        