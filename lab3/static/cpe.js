
function formatDate(dateString){
    const options = {year: "numeric", month: "numeric", day: "numeric"};
    const date = new Date(dateString)
    return date.toLocaleDateString('en-GB', options); 
}
$(document).ready( function () {
    setNavigation();
    //$('#maintable').DataTable();

    console.log("lab3");
    var data=3.1;
    console.log(data);
    data=data+1;
    console.log(data);
    data+=1;
    console.log(data);

    document.getElementById("demo").innerHTML = "Lab 3.1";
    
    var data = document.getElementById("demo").innerHTML; 
    console.log(data + (1 + 1)); 
    document.getElementById("demo").innerHTML = data + (1 + 1);

    $('#demo').text ("Jquery Lab3");

    var data = 3;
    $('#demo').click(function(){ 
        data +=1;
        console.log('on click' + data);
        $(this).text ("Jquery Lab3.1");
    });
    $("H1").click(function() {
        $("H1").text('Change to Lab 3.1'); 
        //$("#demo").load("https://nagatox.github.io/cpe231/allinvoice.json");
        $.get("https://nagatox.github.io/cpe231/allinvoice.json", function(data, status){
            console.log("Data: " + data + "\nStatus: " + status); 
            var total = 0;
            $('#maintable tbody').empty();
            $('#maintable tbody').append('<tr><th>Invoice No</th><th>Date</th><th>Customer Code</th><th>Customer Name</th></th><th>Due Date</th><th>Total</th><th>VAT</th><th>Amount Due</th><th>Product Code</th><th>Product Name</th><th>Quantity</th><th>Unit Price</th><th>Extended Price');
            $.each(data, function (key,val){
                var formattedDate = formatDate(val["Date"]);
                console.log("key: " + key + "\nval: " + val["Extended Price"]);
                $('#maintable tbody').append('<tr><td>' + val["Invoice No"] + '</td>' +
                                                  '<td>' + formattedDate + '</td>' +
                                                  '<td>' + val["Customer Code"] + '</td>' +
                                                  '<td>' + val["Customer Name"] + '</td>' +
                                                  '<td>' + val["Due Date"] + '</td>' +
                                                  '<td>' + val["Total"] + '</td>' +
                                                  '<td>' + val["VAT"] + '</td>' +
                                                  '<td>' + val["Amount Due"] + '</td>' +
                                                  '<td>' + val["Product Code"] + '</td>' +
                                                  '<td>' + val["Product Name"] + '</td>' +
                                                  '<td>' + val["Quantity"] + '</td>' +
                                                  '<td>' + val["Unit Price"] + '</td>' +
                                                  '<td>' + val["Extended Price"].toLocaleString("en-US") + '</td>' +
                                                  '</tr>');
                total += val["Extended Price"];
             });
            $("H1").text("Total Price = " + total);
         });
     });

     console.log('after get:');



    var total = 0;
    $('#maintable tr td').each (function (key,val) {
        if (key % 13 == 12) {
            console.log("key: " + key + "\nval: " + val.innerHTML + "\n" + parseFloat(val.innerHTML));
            total += parseFloat(val.innerHTML);
    }
    $("H1").text("Total Price = " + total); });
} );


function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".nav a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(1, href.length+1) === href) {
            $(this).closest('li').addClass('active');
        }
    });
}