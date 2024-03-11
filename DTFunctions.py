


# Variabelen voor connectie met PosgreSQL-database. 
# Naam van database vanuit het script via instructie PostgreSQL_database: "databasenaam"
psql_host="localhost"           # "127.0.0.1"
psql_user="postgresZIPPER"
psql_password="xxxxxxx"
psql_port="5432"                # defaults to 5432 if it is not provided



# zerofill(1,2) => '01' ; str(1.5).zfill(4) => '01.5' (insert leading zeros)
def zerofill (number, length):
    return str(number).zfill(length)

# strcontains('ABCD', 'BC') => True
def strcontains(str1,str2):                          
    return str2 in str1



















