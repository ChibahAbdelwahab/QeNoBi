$(".customercentric").show();
$(".productcentric").hide()

$("#product-centric-tab").on("click", function () {
    $(".customercentric").hide();
    $(".productcentric").show()

})

$("#customer-centric-tab").on("click", function () {
    $(".customercentric").show();
    $(".productcentric").hide()

})

$('select').selectpicker({
    selectAllText: 'ALL',
});

// Dataset buttons
$('.dataset-buttons button').first().addClass("btn-primary");

$('.dataset-buttons button').on('click', function () { // On the click event for each button
    console.log("Clicked")
    $(".dataset-buttons button").removeClass("btn-primary");
    $(this).addClass("btn-primary");
});
