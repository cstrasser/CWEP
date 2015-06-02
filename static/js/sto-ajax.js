$(document).ready(function() {
alert("TEst");
 $('.dropdown-menu').on('click','status',function(){
        var status;
       
        status = $(this).val();
        alert("Got to here" +status+)
        $.get('/sto/listview/', {status: status}, function(data){
         
         
        // $('#cats').html(data);
        });
});   
    
    
    
    
    

});