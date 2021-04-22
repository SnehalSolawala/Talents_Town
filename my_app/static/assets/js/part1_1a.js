$(document).ready(function(){
    $("#create").click(function(){
      $("#right1").slideUp(1000).delay(1000);
      // $(".right1").slideUp(1000);
      $("#right2").delay(1000).slideDown(2000); 
    });
  })
$(document).ready(function(){
    $("#sign").click(function(){   
      $("#right2").slideUp(2000).delay(3000);   
      $("#right1").delay(3000).slideDown(1000);
    });
  });
