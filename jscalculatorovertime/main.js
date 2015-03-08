
//function caluclate {

    mondayHours = prompt("Please enter the number of hours worked on Monday");
    tuesdayHours = prompt("Please enter the number of hours worked on Tuesday");
    wednesdayHours = prompt("Please enter the number of hours worked on Wednesday");
    thursdayHours = prompt("Please enter the number of hours worked on Thursday");
    fridayHours = prompt("Please enter the number of hours worked on Friday");
    saturdayHours = prompt("Please enter the number of hours worked on Saturday");
    sundayHours = prompt("Please enter the number of hours worked on Sunday");

    hourlyRate = prompt("what is your hourly rate?");
    document.write("Your hourly rate is "+ hourlyRate + ". ");

    overtimeRate = prompt("what is your overtime rate?");
    document.write("Your overtime rate is "+ hourlyRate + ". ");

    totalHours = parseInt(mondayHours) + parseInt(tuesdayHours) + parseInt(wednesdayHours) +parseInt(thursdayHours) + parseInt(fridayHours) + parseInt(saturdayHours) + parseInt(sundayHours);
    document.write("You worked " + totalHours + " hours this week" + ". ");

    overtimeHours = parseInt(totalHours) - 40;
    document.write("You worked " + overtimeHours + " hours of overtime this week. " );

    overtimePay = parseInt(overtimeHours)* parseInt(overtimeRate);
    document.write("You made " + overtimePay + " dollars from overtime this week. ");

    regularPay = parseInt(totalHours) * parseInt(hourlyRate);
    document.write("You worked " + totalHours + " hours this week. ");

    totalPay = parseInt(overtimePay) + parseInt(regularPay);
    document.write("You made " + totalPay + " dollars this week.");



    alert(totalPay);
//}


//    document.write(totalPay)
//    document.write(hourlyRate)
//    document.write(hours)
//



//
//function calculate(){
//    hourlyrate = 20
//
//    while (hours < 10){
//    alert(hours);
//    hours = hours+1}
//
//}
////function calculate(){
//for (var weeklyHours = mondayHours + tuesdayHours + wednesdayHours +thursdayHours + fridayHours; )
//
//    alert(i)}
//function loop() {
//for (var i=0; i<10; i= i +1 ){
//    alert(i)}
//}

//
//
//function loop(){
//    var i=0
//    while (i <10){
//    alert(i);
//    i = i+1}
//
//    }


//
//document.write("Foo bar");
//
//var x;
//var y;
//var z;
//
////x = variable, 5 is a literal
//x = 5;
//y = 10;
//z = x + y;
//
//a = "5"
//b = "10"
//c = parseInt(a) + parseInt(b)
////run srting as int
//
//
//
////no spaces in var names
//
//document.write(z);
//document.write(c);
//document.write(a+b);
//
//
//alert(55);
//
//
//var l = 5;
//var n = 6;
//var m + 66;
//
//
//x = prompt("enter a #")
//y = prompt("feref")
//z = x+y;
//
//alert(z);
//
//
//
//
//function calculate() {
//
//var x;
//var y;
//var z;
//
//x = prompt("enter a #")
//y = prompt("feref")
//z = parseInt(x) + parseInt(y);
//
//
//alert(z);
//
//}
////
////
////
////calculate();
////
//
//
//
//
































