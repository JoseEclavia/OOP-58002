import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\Database1.accdb;')
    print("Connected to a Database")

    Inventor = 'Espares, Lambojo, Golveo, Padriquez, Mercado, Eclavia, Atienza, Rios'
    Invention = 'Connecting MS Access Database'
    DateofInvention = 2022
    Description = "Create a table of notable inventors (hardware or software) of the past. Create a python program that connects Pycharm to MS Access Database."
    user_id = 11

    record = connect.cursor()
    record.execute('UPDATE tblInventor SET Inventor = ?, Invention = ?, DateofInvention = ?, Description = ?, WHERE id = ?', (Inventor, Invention, DateofInvention, Description, user_id))
    record.commit()
    print("Data is inserted")

except pyodbc.Error as e:
    print("Connection Error")