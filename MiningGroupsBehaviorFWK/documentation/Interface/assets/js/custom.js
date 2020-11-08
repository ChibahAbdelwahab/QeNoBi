$('button').on('click', function () {
        $('button').removeClass('active');
        $(this).addClass('active');
    }
);
console.log("HELLLO")
$("#customer-centric-selection").show();
$("#product-centric-selection").hide()

$("#product-centric-tab").on("click", function () {
    $("#customer-centric-selection").hide();
    $("#product-centric-selection").show()

})


$("#customer-centric-tab").on("click", function () {
    $("#customer-centric-selection").show();
    $("#product-centric-selection").hide()

})
      
     
