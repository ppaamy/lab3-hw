
from DBHelper import DBHelper

class ReportUnpaidInvoices:
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

    print ("Report unpaid invoices")
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.invoice_no as "Invoice No", i.date as "Invoice Date" ' 
                              ' , c.name as "Customer Name"'
                              ' ,i.amount_due as "Invoice Amount Due"'
                              ' ,i.amount_due - ('
                              '   SELECT SUM(amount_paid_here)'
                              '   FROM receipt_line_item'
                              '   WHERE invoice_no = i.invoice_no) as "Amount Received"'
                              ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code ')
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


    db = DBHelper()
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(i.amount_due - ('
                              ' SELECT SUM(amount_paid_here)'
                              '   FROM receipt_line_item'
                              '   WHERE invoice_no = i.invoice_no'
                              ' )) as "Total Invoice Amount Not Paid" '
                              ' FROM invoice i'
                              '')
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

