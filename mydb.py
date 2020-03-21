import mysql.connector
import datetime
import time
import mypsw

myconnector = None
mycorsor = None

def add_symbol(symbol_id, symbol_alias):
    st_date_str = datetime.datetime(1949, 12, 31).strftime("%Y-%m-%d")
    
    try:
        myconnector = mysql.connector.connect(
            host=mypsw.host, 
            user=mypsw.user, 
            passwd=mypsw.passwd, 
            database=mypsw.database, 
            auth_plugin='mysql_native_password')
        mycursor = myconnector.cursor()
    except Exception as e:
        print(datetime.datetime.now(), ": Connection :" ,e)
        return 0
    select_log_statment = "SELECT * FROM zeroai.predictlog where symbol = '" + str(symbol_id) + "'"

    try:
        mycursor.execute(select_log_statment)
        log_results = mycursor.fetchall()
    except Exception as e:
        print(datetime.datetime.now(), ": Fetching Log :" ,e)
        return 0
    if len(log_results) > 0:
        return 0

    insert_log_statment = "INSERT INTO zeroai.predictlog (SYMBOL, PREDICTDATE) VALUES ('" + str(symbol_id) + "','" + st_date_str + "');"
    mycursor.execute(insert_log_statment)

    insert_symbol_statment = "INSERT INTO zeroai.symbol_alias (SYMBOL_ALIAS, SYMBOL, MARKET_TYPE, MARKET_ORDER, TITLE_FLAG) VALUES ('" \
    + str(symbol_alias) + "','" + str(symbol_id) + "','加密货币','0','X');"
    mycursor.execute(insert_symbol_statment)
    myconnector.commit()
    return 1
