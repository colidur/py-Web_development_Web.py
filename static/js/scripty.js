
$(document).ready(function(){
  console.log("loaded");
  var util = require(Util);
  $('body').bootstrapMaterialDesign();
  $(document).on("submit ","#register-form",function(e){
    e.preventDefault();

    var form=$('#register-form').serialize();
    $.ajax({
       url:'/Postregistration',
      type:'POST',
      data:'form',
      sucess:function(reponse){
        console.log(response);
      }
    });
  });
});
