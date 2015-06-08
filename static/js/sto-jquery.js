$(document).ready(function() {

//http://stackoverflow.com/questions/9127498/how-to-perform-a-real-time-search-and-filter-on-a-html-table
//http://jsfiddle.net/7BUmG/2/
    
var $rows = $('#mytable tr');
$('#search_item').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
    
    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
});
   
   
 $("#rental_filter").on('click',function(){
 // $(".stoitem, td").hide();
   //$( ".stoitem, td" ).each(function( i ) {
    $( "#billtype" ).each(function( i ) {
    //if ( this.style.color !== "green" ) {
    if (this.text == "Rental" ) {
      this.style.color = "green";
      //alert(this.text);
    } else {
      this.style.color = "blue";
      }
  });  
});
    
    
    
  
 
 $("#warranty_filter").on('click',function(){
    //default each row to visible
     $('.stoitem, td').show();
     
    var $rowsNo = $('#mytable tbody tr').filter(function () {
        return $.trim($(this).find('td').eq(7).text()) !== "Warranty"}).toggle();

   
});
 
    
 $("#bill_filter").on('click',function(){
    $(".stoitem, td").hide()    
});
 

  
      
            
    }); //doc ready 


//Commission
//Upkeep
//No Charge
//Project
//Non-Bill
//Bill
//System
//Sales
//Contract
//Unknown
//Included
//Warranty
//Unkown
//Rental
//Telemetry
//RMA






