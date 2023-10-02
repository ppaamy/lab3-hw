
from DBHelper import DBHelper

class ReportListAllReceipts:
    pass

def Report():
    print ("""<html>
                <head>
                    <title>Report Invoice</title>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="static/cpe.js"></script>
                    <link rel='stylesheet' href='static/cpe.css'>
                </head>
                <body><H1>Report Invoice.</H1>
                <ul class="nav">
                    <li><a href="/index.html">Main</a></li>
                    <li><a href="ReportListAllInvoices">Report list all invoices</a></li>
                    <li><a href="ReportProductsSold">Report products sold</a></li>
                    <li><a href="ReportListAllProducts">Report list all products</a></li>
                    <li><a href="ReportListAllReceipts">Report list all receipts</a></li>
                    <li><a href="ReportUnpaidInvoices">Report unpaid invoices</a></li>
                    <li><a href="ReportListAllCustomers">Report list all customers</a></li>
                </ul>
                <div id='div-lab3'></div>
                """)

    print ("Report list all receipts")
    db = DBHelper()
    data, columns = db.fetch ('SELECT r.receipt_no as "Receipt No", rt.invoice_no as "Invoice No" ' 
                              ' , r.customer_code as "Customer Code", c.name as "Customer Name"'
                              ' , r.total_received as "Total Receipt", r.payment_method as "Payment Menthod" '
                              ' , r.date as "Date", r.payment_reference as "Payment reference" , r.remarks as "Remarks"'
                              ' FROM receipt r JOIN receipt_line_item rt ON r.receipt_no = rt.receipt_no '
                              ' JOIN invoice i ON rt.invoice_no = i.invoice_no ' 
                              ' JOIN customer c ON c.customer_code = r.customer_code '
                              ' ')
    print ("<table id='maintable' class='display table-lab3'>")
    print ("<tr>")
    for col in columns: 
        print ("<th>" + col + "</th>")
    print ("</tr>")
    
    for row in data: 
        print ("<tr>")
        for col in row:
            print ("<td>" + str(col) + "</td>")
        print ("</tr>")
    print ("</table>")
    print ("</body></html>")