
from DBHelper import DBHelper

class ReportListAllCustomers:
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

    print ("Report list all customers")
    db = DBHelper()
    data, columns = db.fetch ('SELECT  c.name as "Customer Name", i.customer_code as "Customer Code", SUM(i.amount_due) as "Total Amount" '
                              ' FROM invoice as i, customer as c '
                              ' WHERE (i.customer_code,c.name) IN (SELECT i.customer_code, c.name '
						      '     FROM invoice as i, customer as c '
						      '     WHERE i.customer_code = c.customer_code)'
                              ' GROUP BY i.customer_code, c.name '
                              ''  )
    
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