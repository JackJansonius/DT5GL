

# The functions below for calculation with dates are already loaded in DT.exe and thus available within the scripts:


# ########## functions for formulas for calculating with datums  #3.53# ##############
from datetime import datetime, timedelta            #3.53# rekenen met datums..
from dateutil.relativedelta import relativedelta
# Attribute: Client.Geboortedatum  Type: Text (= datumtekst ('yyyy-mm-dd') in de database). 
# A. From datetime to integer for use in conditions and conclusions:                to_integer(fdatum(Client.Geboortedatum) + fdeltaweken(4))
# B. From datetime to date text to write away to database (sqlite):                 fdatum_naar_datumtekst(fdatum(Client.Geboortedatum) + fdeltamaanden(14)) 
# C. From integer to date text to write out to database (sqlite):                   integer_naar_datumtekst(Datum_vanaf_SV1)
# D. As A, but without adding a period:                                             to_int(Onderdeel_D.Datum_vanaf)
#
# Also exists a "psql_" version of B and C for writing to postgreSQL database (dates between singelquotes instead of doublequotes). 



def fdatum (datumtekst):                                           # converts date in format 'yyyy-mm-dd' to datatype datetime so that a new date can be determined with relativedelta.
    return datetime.strptime(datumtekst, '%Y-%m-%d')

def fdeltadagen(n):
    return relativedelta(days=n)

def fdeltaweken(n):
    return relativedelta(weeks=n)
    
def fdeltamaanden(n):
    return relativedelta(months=n)
    
def fdeltajaren(n):
    return relativedelta(years=n)

def fdatumnaarstring(n):
    return str(n)[0:10]

def to_integer(dt_time):                                            # to_integer(fdatum(Client.Geboortedatum) + fdeltaweken(4))
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

def integer_naar_datumtekst (inwaarde):                             # integer_naar_datumtekst(Datum_vanaf_SV1) / tussen dubbelquotes (sqlite)
    b=str(inwaarde)                                                 # voor schrijven naar database.
    if len(b) == 8:
        return '"'+b[0:4]+"-"+b[4:6]+"-"+b[6:8]+'"'      
    else:
        return '"0000-00-00"'

def psql_integer_naar_datumtekst (inwaarde):                        # integer_naar_datumtekst(Datum_vanaf_SV1) / tussen singelquotes (postgresql)
    b=str(inwaarde)                                                 # voor schrijven naar database. 
    if len(b) == 8:
        return "'"+b[0:4]+'-'+b[4:6]+'-'+b[6:8]+"'"      
    else:
        return "'0000-00-00'"

        
def fdatum_naar_datumtekst(x):                                      # fdatum_naar_datumtekst(fdatum(Client.Geboortedatum) + fdeltamaanden(14))
    return integer_naar_datumtekst(to_integer(x))

    
def psql_fdatum_naar_datumtekst(x):                                 # fdatum_naar_datumtekst(fdatum(Client.Geboortedatum) + fdeltamaanden(14))
    return psql_integer_naar_datumtekst(to_integer(x))    
    
  

def to_int(dt_text):                                                # zet datum in formaat 'yyyy-mm-dd' om naar integer: to_int(Onderdeel_D.Datum_vanaf)
    return int(dt_text.replace('-',''))


def integer_naar_fdatuminput (x):                                   # integer naar kale datumtekst zonder omsluitende quotes als input voor fdatum. 
    b=str(x)
    if len(b) == 8:
        return b[0:4]+'-'+b[4:6]+'-'+b[6:8]      
    else:
        return '0000-00-00'


def leeftijd_op_uitvoerdatum (uitvoerdatum, geboortedatum):         # datumformaten: 'yyyy-mm-dd'
    return relativedelta(datetime.strptime(uitvoerdatum, "%Y-%m-%d"), datetime.strptime(geboortedatum, "%Y-%m-%d")).years


###################################################################################

import time
    
def waiting(seconds):
    time.sleep(seconds)
    return 1


