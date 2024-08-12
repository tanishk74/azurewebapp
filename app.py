from flask import Flask, render_template
import pandas as pd
import pypyodbc as odbc
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('task1.html')

@app.route('/task2')
def task2():


    server = 'bootcampaug5server.database.windows.net'
    database = 'bootcampaug5db'
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:bootcampaug5server.database.windows.net,1433;Database=bootcampaug5db;Uid=bootcamp;Pwd=Pass@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=200;'
 
    conn = odbc.connect(connection_string)
    sql = '''
    select top 20 * from [SalesLT].[Customer]
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    databaseFetched = cursor.fetchall()
    datasetCol = [col[0] for col in cursor.description]
    df = pd.DataFrame(databaseFetched,columns = datasetCol)

    return render_template('task2.html', tables=[df.to_html(classes='data', header="true")])

@app.route('/task3')
def task3():
    server = 'bootcampaug5server.database.windows.net'
    database = 'bootcampaug5db'
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:bootcampaug5server.database.windows.net,1433;Database=bootcampaug5db;Uid=bootcamp;Pwd=Pass@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=200;'
 
    conn = odbc.connect(connection_string)
    sql = '''
    SELECT
                p.Name AS ProductName, p.Color, p.Size, p.Weight
                FROM SalesLT.Product p
                JOIN SalesLT.ProductCategory pc
                ON
                p.ProductCategoryID = pc.ProductCategoryID
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    databaseFetched = cursor.fetchall()
    datasetCol = [col[0] for col in cursor.description]
    df = pd.DataFrame(databaseFetched,columns = datasetCol)

    return render_template('task3.html', tables=[df.to_html(classes='data', header="true")])



if __name__ == '__main__':
    app.run(debug=True)