$(document).ready(function() {

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
    
   
    //$.get('/sto/listview/',  function(stat){  
 
 
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

//http://stackoverflow.com/questions/15688147/hide-row-in-table-based-on-td-cell-in-another-row-using-jquery
//https://api.jquery.com/category/traversing/filtering/
// }).parent('tr').css('color','red');

//var code = e.keyCode || e.which;
// if(code == 13) { //Enter keycode
//   //Do something
// }

//http://stackoverflow.com/questions/12385343/jquery-show-hide-table-rows-based-on-cell-content   
     
      
      //alert($(".stoitem").parent('a').val);
     // $( "li" ).not( ":even" ).css( "background-color", "red" );
     // $( ".stoitem, tr:contains('201')" ).show('tr');
      //$( "td:contains('20190')" ).show();







