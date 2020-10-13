"""
Created on Fri Aug 30 12:06:44 2019

@author: stefflc
"""


'''
This file is created to test creation of quotes in the Visual SystemError
The main components of a quote are from tables:
    1. CUSTOMER
    2. QUOTE (Quote is QuoteID + entire CUSTOMER )
    3. QUOTE_LINE
    4. QUOTE_PRICE

    '''
import pyodbc
import traceback
import datetime
import getpass
import re


class testQuote():




#     def init():
# ##
#         a=1

    def main():
        # john = testQuote()

        server = 'MSAVMFG1'
        database = 'VMLIVE'
        #            database = 'MSA712'
        username = 'stefflc'
        password = 'buttpain1'
        cnxn = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        cursor = cnxn.cursor()


##Quote constraints###
    # '''
    # SELECT
    # name, definition 
    # FROM
    #     sys.check_constraints
    # WHERE 
    # name = 'CHK_QUOTE'


    #Status codes
    ##A
    ##R
    ##P
    ##A = in house start here
    ##P = printed


    # (([STATUS] = 'A' or [STATUS] = 'R' or [STATUS] = 'P' 
    #   or [STATUS] = 'W' or [STATUS] = 'L' or [STATUS] = 'X')
    
    #     and ([TERMS_NET_TYPE] = 'A' or [TERMS_NET_TYPE] = 'M' 
    #     or [TERMS_NET_TYPE] = 'D' or [TERMS_NET_TYPE] = 'N'
    #     or [TERMS_NET_TYPE] = 'E' or [TERMS_NET_TYPE] = 'I')
    
    #     and ([TERMS_DISC_TYPE] = 'A' or [TERMS_DISC_TYPE] = 'M'
    #          or [TERMS_DISC_TYPE] = 'D' or [TERMS_DISC_TYPE] = 'N' 
    #          or [TERMS_DISC_TYPE] = 'E')
    
    #     and ([FREIGHT_TERMS] = 'P' or [FREIGHT_TERMS] = 'B' 
    #     or [FREIGHT_TERMS] = 'C'))
    # '''
        print("ehllo")



        quoteNumber = 'CES001'
        customerID = 'PWA001'
        cursor.execute('''SELECT TERMS_NET_TYPE, TERMS_DISC_TYPE, FREIGHT_TERMS,
                          NAME, ADDR_1, ADDR_2, ADDR_3, CITY, STATE, ZIPCODE,
                          COUNTRY, CONTACT_FIRST_NAME, CONTACT_LAST_NAME,
                          CONTACT_INITIAL, CONTACT_POSITION, CONTACT_HONORIFIC,
                          CONTACT_SALUTATION, CONTACT_PHONE, CONTACT_FAX


                       FROM CUSTOMER WHERE ID = ?''', customerID)
        cat = cursor.fetchall()
        termsNetType = cat[0][0]
        print("termsNetType: ", termsNetType)
        termsDiscType = cat[0][1]
        print("termsDiscType", termsDiscType)
        freightTerms = cat[0][2]
        print("freightTerms: ", freightTerms)
        customer = cat[0][3]
        addr1 = cat[0][4]
        addr2 = cat[0][5]
        addr3 = cat[0][6]
        city = cat[0][7]
        state = cat[0][8]
        zipcode = cat[0][9]
        country = cat[0][10]
        contactFirstName = cat[0][11]
        contactLastName = cat[0][12]
        contactInitial = cat[0][13]
        contactPosition = cat[0][14]
        contactHonorific = cat[0][15]
        contactSalutation = cat[0][16]
        contactPhone = cat[0][17]
        contactFax = cat[0][18]

        quote_date = datetime.datetime(2019,9,3)#datetime object yyyy-mm-dd - 00s
        print("quote_date: ", quote_date)
        userid= getpass.getuser()
        print("userid: ", userid)
        siteid = 'MSA'
        status = 'A'




        ###example quote###
        ###Find highest quote ID
        try:
            cursor.execute(''' SELECT TOP 1 * FROM QUOTE WHERE ID LIKE 'CES%' ORDER BY ID DESC''')
            allID = cursor.fetchall()
            print("allID: ", allID)




            if (not allID):
                print("if")
                quoteID = 'CES001'
                cursor.execute(''' INSERT INTO QUOTE (ID, CUSTOMER_ID, QUOTE_DATE, 
                                USER_ID, SITE_ID, TERMS_NET_TYPE, TERMS_DISC_TYPE,
                                FREIGHT_TERMS, STATUS,
                                NAME, ADDR_1, ADDR_2, ADDR_3, CITY, STATE,
                                ZIPCODE, COUNTRY, CONTACT_FIRST_NAME,
                                CONTACT_LAST_NAME, CONTACT_INITIAL, CONTACT_POSITION,
                                CONTACT_HONORIFIC, CONTACT_SALUTATION, CONTACT_PHONE,
                                CONTACT_FAX



                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,
                                ?, ?, ?, ?, ?, ?,
                                ?, ?, ?,
                                ?, ?, ?,
                                ?, ?, ?,
                                ?)''', (quoteID, customerID, quote_date, userid,\
                                siteid, termsNetType, termsDiscType, freightTerms, status,\
                                customer, addr1, addr2, addr3, city, state, \
                                zipcode, country, contactFirstName, contactLastName,\
                                contactInitial, contactPosition, contactHonorific,\
                                contactSalutation, contactPhone, contactFax\
                                )  )
                cnxn.commit() #Finalize the insert
            else:
                print("else")

                quoteID = allID[0][1]
                m = re.search(r'\d+$', quoteID)
                if m:
                    quoteCounter = str(m.group())
                    print("quoteCounter: ", quoteCounter)
                    quoteCounter = int(quoteCounter) + 1
                    quoteCounter = str(quoteCounter).zfill(3)
                    print("quoteCounter: ", quoteCounter)


                # quoteObject = allID[0]

                print("quoteID: ", quoteCounter)
                quoteID = 'CES' + quoteCounter
                print("quoteID: ", quoteID)

                cursor.execute(''' INSERT INTO QUOTE (ID, CUSTOMER_ID, QUOTE_DATE, 
                                USER_ID, SITE_ID, TERMS_NET_TYPE, TERMS_DISC_TYPE,
                                FREIGHT_TERMS, STATUS,
                                NAME, ADDR_1, ADDR_2, ADDR_3, CITY, STATE,
                                ZIPCODE, COUNTRY, CONTACT_FIRST_NAME,
                                CONTACT_LAST_NAME, CONTACT_INITIAL, CONTACT_POSITION,
                                CONTACT_HONORIFIC, CONTACT_SALUTATION, CONTACT_PHONE,
                                CONTACT_FAX



                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,
                                ?, ?, ?, ?, ?, ?,
                                ?, ?, ?,
                                ?, ?, ?,
                                ?, ?, ?,
                                ?)''', (quoteID, customerID, quote_date, userid,\
                                siteid, termsNetType, termsDiscType, freightTerms, status,\
                                customer, addr1, addr2, addr3, city, state, \
                                zipcode, country, contactFirstName, contactLastName,\
                                contactInitial, contactPosition, contactHonorific,\
                                contactSalutation, contactPhone, contactFax\
                                )  )
                cnxn.commit() #Finalize the insert

    
            # cursor.execute(''' SELECT * FROM CUSTOMER WHERE ID = 'PWA001' ''')
            # allCustomer = cursor.fetchall()
            # print("allcustomer: ", allCustomer)
        except Exception as ex:
            # john = testQuote()
            # self.printError(ex)
            print(ex)

        try:
            cnxn.close()
        except Exception as ex:
            john = testQuote()
            john.printError(ex)


    def testCursor():
        try:
            cursor = testQuote.connectVisual()
    
            cursor.execute('''SELECT * FROM LABOR_TICKET
                               WHERE TRANSACTION_ID = '4076099'
                               ORDER BY TRANSACTION_ID DESC''')
    
            bill = cursor.fetchall()
            print("bill: ", bill)
        except Exception as ex:
            testQuote.printError(ex)

    def printError(ex):
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        traceback.print_exc()


    # def connectVisual():
    #     try:

    #         ##Connect to Visual


            


    #         return cursor
    #     except Exception as ex:
    #         testQuote.printError(ex)
    if __name__ == "__main__":
        main()