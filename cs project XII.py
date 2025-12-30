def again():
    import os
    from datetime import date
    today=date.today()
    currentmonth=today.month
    day=today.day
    year=today.year

    import pymysql as p
    class color:
        PURPLE = '\033[95m'
        WHITE = '\033[0;37m\]'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        BLACK = "\033[0;30m"
        GREEN = "\033[0;32m"
        BROWN = "\033[0;33m"
        LIGHT_GRAY = "\033[0;37m"
        DARK_GRAY = "\033[1;30m"
        LIGHT_RED = "\033[1;31m"
        LIGHT_GREEN = "\033[1;32m"
        LIGHT_BLUE = "\033[1;34m"
        LIGHT_PURPLE = "\033[1;35m"
        LIGHT_CYAN = "\033[1;36m"
        LIGHT_WHITE = "\033[1;37m"
        FAINT = "\033[2m"
        ITALIC = "\033[3m"
        BLINK = "\033[5m"
        NEGATIVE = "\033[7m"
        CROSSED = "\033[9m"
        WHITE_HIGHLIGHT = '\033[100m'
        RED_HIGHLIGHT = '\033[101m'
        YELLOW_HIGHLIGHT = '\033[103m'
        LIGHT_BLUE_HIGHLIGHT = '\033[104m'
        PURPLE_HIGHLIGHT = '\033[105m'
        END = '\033[0m'
    os.system('cls')
    print('\n\n')
    print(color.PURPLE+color.BOLD+color.UNDERLINE+'\t\t ---APPLE STORE---\t\t\t'+color.END)
    print('\n****************************************************************************\n')
    print(color.PURPLE+color.BOLD+color.UNDERLINE+"\t\tWELCOME TO OUR STORE!"+color.END)
    print("\n---------------------------------------------------------------------------\n")

    print("date= ",today)



    name=input(color.CYAN+"\nENTER YOUR NAME:")
    idd=input(color.BROWN+"ENTER YOUR PHONE NUMBER:")

    con=p.connect(host="localhost",user="root",password="1234",database='store')
    cur=con.cursor()
    q="select * from items;"
    cur.execute(q)
    data=cur.fetchall()
        
    print("\n\n*********************************************************************")

    print(color.LIGHT_BLUE+"\n1)WANT TO VIEW ITEM LIST\n2)IF YOU WANT TO BUY A PHONE\n3)IF YOU WANT TO BUY OTHER PRODUCTS\n4)IF YOU WANT TO GET YOUR PRODUCT REPAIRED \n5)RETURN \n6)OLD PHONE EXCHANGE ")
    A=int(input(color.LIGHT_GREEN+"\nENTER YOUR PREFERENCE:"+color.END))
    print('\n')
    
    if(A==1):
        q="select * from items;"
        cur.execute(q)
        data=cur.fetchall()
        print(" MODEL NUMBER\t\tMODEL NAME\t\t  AVAILABILITY \t\t QUANTITY")
        for i in data:
            print('\n',color.BROWN+(f'{i[0]:^15} {i[1]:^26} {i[2]:^20} {i[3]:^8}')+color.END)
        again()    
    if(A==2):
        q1="select * from items2;"
        cur.execute(q1)
        data1=cur.fetchall()
        print("   SNO\t\tMODEL NAME\t 64GB PRICE\t 128GB PRICE\t 256GB PRICE")
        for i in data1:
            print('\n',f'{i[0]:^10} {i[1]:^20} {i[2]:^15} {i[3]:^15} {i[4]:^10}')
        k=input(color.LIGHT_GRAY+"\nENTER THE PRODUCT YOU WANT:")
        print(color.LIGHT_CYAN+"\nPlease select the amount of 'GB' you want :\n1:64GB\n2:128GB\n3:256GB")
        a=int(input("\nEnter your preference:"+color.END))
        for i in data1:
            for j in i:
                if(j==k):
                    if(a==1):
                        print(color.LIGHT_PURPLE+"\nThe amount for your product is:",i[2])
                        x=i[2]
                    if(a==2):
                        print(color.LIGHT_PURPLE+"\nThe amount for your product is:",i[3])
                        x2=i[3]
                    if(a==3):
                        print(color.LIGHT_PURPLE+"\nThe amount for your product is:"+color.END,i[-1])
                        x3=i[-1]          
        print(color.LIGHT_CYAN+"\nSelect the mode of payment:\n1:Cash\n2:Online payment\n3:EMI"+color.END)
        c=int(input("\nEnter your preference:"))
        if(c==1):
            print(color.BROWN+color.BOLD+color.UNDERLINE+"\n\nYOUR ORDER IS PLACED")
            print("THANK YOU FOR VISITING OUR STORE")
        if(c==2):
            print("\n\nYOUR ORDER IS PLACED")
            print("THANK YOU FOR VISITING OUR STORE"+color.END)
        if(c==3):
            print(color.GREEN+"\nPick you preference: \n1:6 months instalment\n2:8 months instalment"+color.END)
            b=int(input("Enter your preference:"))
            if(b==1):
                if(a==1):
                    g=x//6
                    print(color.BOLD+"\nYour monthly payment is",g)
                if(a==2):
                    f=x2//6
                    print(color.BOLD+"\nYour monthly payment is",f)
                if(a==3):
                    t=x3//6
                    print(color.BOLD+"\nYour monthly payment is",t)
                    
            if(b==2):
                if(a==1):
                    g=x//8
                    print(color.BOLD+"\nYour monthly payment is",g)
                if(a==2):
                    f=x2//8
                    print(color.BOLD+"\nYour monthly payment is",f)
                if(a==3):
                    t=x3//8
                    print(color.BOLD+"\nYour monthly payment is:",t)
        #BILLING
        bil='select max(bill_no) from billing;'
        cur.execute(bil)
        data3=cur.fetchone()
        x=data3[0]
        bill=x+1
        z2="insert into billing values('{}','{}','{}','{}',{});".format(name,idd,k,today,bill)
        cur.execute(z2)
        con.commit()             
        #insaurance
        if(currentmonth in (1,3,5,7,8,10,12)):
            if(currentmonth in (1,8)):
                if(day==1):
                    c1=currentmonth-1
                    y1=year+1
                    d1=31
                    i1=date(y1,c1,d1)
                    print(color.BROWN+"YOUR PRODUCT'S WARRANTY IS VALID TILL-",i1)
                    Z0="insert into validity values('{}',{},'{}');".format(k,bill,i1)
                    cur.execute(Z0)
                    con.commit()
            elif(day==1):
                d1=30
                c1=currentmonth-1
                y1=year+1
                i2=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i2)
                Z0="insert into validity values('{}',{},'{}');".format(k,bill,i2)
                cur.execute(Z0)
                con.commit()
            else:
                c1=currentmonth-1
                y1=year+1
                d1=day-1
                i5=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i5)
                Z0="insert into validity values('{}',{},'{}');".format(k,bill,i5)
                cur.execute(Z0)
                con.commit()
            if((year+1)%4==0):
                if(currentmonth==3):
                    if(day==1):
                        d1=29
                        c1=currentmonth-1
                        y1=year+1
                        i3=date(y1,c1,d1)
                        print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i3)
                        Z0="insert into validity values('{}',{},'{}');".format(k,bill,i3)
                        cur.execute(Z0)
                        con.commit()

            else:
                if(currentmonth==3):
                    d1=28
                    c1=currentmonth-1
                    y1=year+1
                    i4=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i4)
                    Z0="insert into validity values('{}',{},'{}');".format(k,bill,i4)
                    cur.execute(Z0)
                    con.commit()
        else:
            if(day==1):
                c1=currentmonth-1
                y1=year+1
                d1=31
                i6=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i6)
                Z0="insert into validity values('{}',{},'{}');".format(k,bill,i6)
                cur.execute(Z0)
                con.commit()
                
            else:
                c1=currentmonth-1
                y1=year+1
                d1=day-1
                i7=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-"+color.END,i7)
                Z0="insert into validity values('{}',{},'{}');".format(k,bill,i7)
                cur.execute(Z0)
                con.commit()
                    
                    
        print(color.YELLOW+color.UNDERLINE+color.BOLD+"\t\t\n\nTHANKS FOR VISITING OUR STORE\nHOPE YOU HAD A GREAT EXPERIENCE"+color.END)
        #receipt
        os.system('cls')
        print(color.PURPLE_HIGHLIGHT+color.BOLD+color.ITALIC+'\t\tAPPLE STORE\t\t\t\t'+color.END)
        print('ADDRESS:17/46A subhash nagar , new delhi')
        print('\t\tTelp:11223345')
        print('************************************************')
        print('\t\tCASH RECEIPT')
        print('************************************************')
        print('Description')
        print('\nNAME       =\t',name)
        print('PHONE NUMBER =\t',idd)
        print('PRODUCT      =\t',k,'\t')
        print('BILL NUMBER  =\t',bill,'\n')
        print(color.LIGHT_BLUE_HIGHLIGHT+'\t\t\tTHE END\t\t\t'+color.END)
        input()
        t="select * from items where model_name='{}';".format(k)
        cur.execute(t)
        con.commit()
        ft=cur.fetchone()
        n=ft[3]
        n1=n-1
        n=n1
        s="update items set quantity={} where model_name='{}';".format(n1,k)
        cur.execute(s)
        con.commit()
        again()
        
        
    if(A==3):
        q2="select * from accessories;"
        cur.execute(q2)
        data2=cur.fetchall()
        print(" Sno\t\tMODEL NAME\t\t COLOR\t\t\tPRICE")
        for i in data2:
            print('\n',color.LIGHT_PURPLE+f'{i[0]:^6} {i[1]:^25} {i[2]:^22}{i[3]:^20}')
        k1=input(color.LIGHT_GRAY+"\nENTER THE PRODUCT YOU WANT:")
        print(color.LIGHT_BLUE+"PLEASE SELECT THE COLOR YOU WANT:")
        u=input("ENTER THE COLOR:")
        for i in data2:
            for j in i:
                if(j==k1):
                    if(i[2]==u):
                        print(color.YELLOW+"\nTHE PRICE OF YOUR PRODUCT IS:"+color.END,i[3])
                        z=i[3]
        print(color.LIGHT_CYAN+"\nSelect the mode of payment:\n1:Cash\n2:Online payment\n3:EMI"+color.END)
        d=int(input("\nEnter your preference:"))
        if(d==1):
            print(color.BROWN+color.BOLD+color.UNDERLINE+"\n\nYOUR ORDER IS PLACED")
            print("THANK YOU FOR VISITING OUR STORE")
        if(d==2):
            print("\n\nYOUR ORDER IS PLACED")
            print("THANK YOU FOR VISITING OUR STORE"+color.END)
        if(d==3):
            print(color.GREEN+"\nPick you preference: \n1:6 months instalment\n2:8 months instalment"+color.END)
            y=int(input("Enter your preference:"))
            if(y==1):
                q=z//6
                print(color.LIGHT_GRAY+"YOUR MONTHLY INSTALLMENT IS-",q)
                print("\t\tTHANK YOU FOR VISITING OUR STORE")
            if(y==2):
                w=z//8
                print("YOUR MONTHLY INSTALLMENT IS-",w)
                print("\t\tTHANK YOU FOR VISITING OUR STORE"+color.END)
        #BILLING
        bil='select max(bill_no) from billing;'
        cur.execute(bil)
        data3=cur.fetchone()
        x=data3[0]
        bill=x+1
        z1="insert into billing values('{}','{}','{}','{}',{});".format(name,idd,k1,today,bill)
        cur.execute(z1)
        con.commit()
        
        #insaurance
        if(currentmonth in (1,3,5,7,8,10,12)):
            if(currentmonth in (1,8)):
                if(day==1):
                    c1=currentmonth-1
                    y1=year+2
                    d1=31
                    i1=date(y1,c1,d1)
                    print(color.LIGHT_GREEN+"YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i1)
                    z0="insert into validity values('{}',{},'{}');".format(k1,bill,i1)
                    cur.execute(z0)
                    con.commit()
     
            elif(day==1):
                d1=30
                c1=currentmonth-1
                y1=year+2
                i2=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i2)
                z0="insert into validity values('{}',{},'{}');".format(k1,bill,i2)
                cur.execute(z0)
                con.commit()
     
            else:
                c1=currentmonth-1
                y1=year+2
                d1=day-1
                i5=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i5)
                z8="insert into validity values('{}',{},'{}');".format(k1,bill,i5)
                cur.execute(z8)
                con.commit()
     
            if((year+1)%4==0):
                if(currentmonth==3):
                    if(day==1):
                        d1=29
                        c1=currentmonth-1
                        y1=year+2
                        i3=date(y1,c1,d1)
                        print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i3)
                        z0="insert into validity values('{}',{},'{}');".format(k1,bill,i3)
                        cur.execute(z0)
                        con.commit()
     

            else:
                if(currentmonth==3):
                    d1=28
                    c1=currentmonth-1
                    y1=year+2
                    i4=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i4)
                    z0="insert into validity values('{}',{},'{}');".format(k1,bill,i4)
                    cur.execute(z0)
                    con.commit()
     
        else:
            if(day==1):
                c1=currentmonth-1
                y1=year+2
                d1=31
                i6=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i6)
                z0="insert into validity values('{}',{},'{}');".format(k1,bill,i6)
                cur.execute(z0)
                con.commit()
            else:
                c1=currentmonth-1
                y1=year+2
                d1=day-1
                i7=date(y1,c1,d1)
                print("YOUR PRODUCT'S WARRANTY IS VALID TILL-\n"+color.END,i7)
                z0="insert into validity values('{}',{},'{}');".format(k1,bill,i7)
                cur.execute(z0)
                con.commit()
     
        #receipt
        os.system('cls')
        print(color.PURPLE_HIGHLIGHT+color.BOLD+color.ITALIC+'\t\tAPPLE STORE\t\t\t\t'+color.END)
        print('\tADDRESS:17/46A subhash nagar , new delhi')
        print('\t\tTelp:11223345')
        print('************************************************')
        print('\t\tCASH RECEIPT')
        print('************************************************')
        print('Description\t\t\tPRICE')
        print('\nNAME\t     =\t',name)
        print('PHONE NUMBER =\t',idd)
        print('PRODUCT      =\t',k1,'\t',z)
        print('BILL NUMBER  =\t',bill,'\n')      
        print(color.LIGHT_BLUE_HIGHLIGHT+'\t\t\tTHE END\t\t\t'+color.END)
        input()
        t="select * from items where model_name='{}';".format(k1)
        cur.execute(t)
        con.commit()
        ft=cur.fetchone()
        n=ft[3]
        n1=n-1
        n=n1
        s="update items set quantity={} where model_name='{}';".format(n1,k1)
        cur.execute(s)
        con.commit()
        again()

    #REPAIR
    if(A==4):
        print(color.LIGHT_BLUE+"VERIFY THE PRODUCT YOU WANT TO REPAIR")
        I=input("ENTER:"+color.END)
        print(color.DARKCYAN+"\nPLEASE SPECIFY THE ISSUE BELOW")
        p=input("ENTER:"+color.END)
        p1=int(input(color.LIGHT_RED+"\nENTER YOUR BILL NO:"+color.END))
        o='select * from billing where bill_no={};'.format(p1)
        cur.execute(o)
        con.commit()
        data4=cur.fetchone()
        a1=data4[4]
        a2=data4[3]
        O='select * from validity where bill_no={};'.format(p1)
        cur.execute(O)
        con.commit()
        data5=cur.fetchone()
        
        a3=data5[2]
        if(a1==p1):
            print(color.PURPLE+'\nYOUR DATE OF PURCHASE WAS:'+color.END,a2)
            print(color.PURPLE+'\nYOUR INSAURANCE IS VALID TILL'+color.END,a3)
            if(a3<=today):
                print(color.PURPLE+'\nYOUR INSAURANCE HAS BEEN EXPIRED')
                print('YOU HAVE TO PAY FULL AMOUNT FOR THE REPAIR')
                print('YOU WILL BE NOTIFIED AS SOON AS YOUR PRODUCT IS REPAIRED'+color.END)
            else:
                print(color.PURPLE+'\nYOUR PRODUCT IS STILL IN WARRANTY')
                print('SO YOUR SERVICE IS FREE')
                print('YOU WILL BE NOTIFIED AS SOON AS YOUR PRODUCT IS REPAIRED'+color.END)
        else:
            print(color.PURPLE+'BILL NO IS INCORRECT'+color.END)
        os.system('cls')
        input()
        again()
            
    #RETURN
    if(A==5):
        n1=int(input(color.RED+"ENTER YOUR BILL NO:"+color.END))
        r='select * from billing where bill_no={};'.format(n1)
        cur.execute(r)
        con.commit()
        data6=cur.fetchone()
        t=data6[3]
        t1=t.day
        t2=t1+7
        if(t1<=t2):
            print(color.CYAN+'\nYOU CAN RETURN THE PRODUCT')
            print('SORRY FOR THE INCONVENIENCE'+color.END)
        else:
            print(color.CYAN+'\nYOUR RETURN POLICY IS OVER YOU CANNOT RETURN THE PRODUCT'+color.END)
        os.system('cls')
        input()
        again()
            
    #OLD PHONE EXCHANGE        
    if(A==6):
        s=input(color.LIGHT_PURPLE+"ENTER THE PHONE YOU WANT TO EXCHANGE:"+color.END)
        print(color.YELLOW+'\nCHECK THE ITEMS YOU WANT TO BUY\n'+color.END)
        print(color.PURPLE_HIGHLIGHT+'!!!THERE IS A 15% OFF ON BUYING A PHONE!!!'+color.END)
        print(color.PURPLE_HIGHLIGHT+'!!!AND 8% OFF ON OTHER PRODUCTS!!!'+color.END)
        q1="select * from items2;"
        cur.execute(q1)
        data1=cur.fetchall()
        print("\n   SNO\t\tMODEL NAME\t 64GB PRICE\t 128GB PRICE\t 256GB PRICE")
        for i in data1:
                print(color.LIGHT_PURPLE+'\n',f'{i[0]:^10} {i[1]:^20} {i[2]:^15} {i[3]:^15} {i[4]:^10}'+color.END)
        q2="select * from accessories;"
        cur.execute(q2)
        data2=cur.fetchall()
        print("\n\n  SNO\t\tMODEL NAME\t\t COLOR\t\t\tPRICE")
        for i in data2:
                print('\n',color.LIGHT_PURPLE+f'{i[0]:^6} {i[1]:^25} {i[2]:^22}{i[3]:^20}'+color.END)
        e=input("\nENTER THE PRODUCT YOU WANT TO BUY:")
        if('iphone' in e):
            print(color.LIGHT_CYAN+"\nPlease select the amount of 'GB' you want :\n1:64GB\n2:128GB\n3:256GB")
            a=int(input("\nEnter your preference:"+color.END))
            
            for i in data1:
                for j in i:
                    if(j==e):
                        if(a==1):
                            x=i[2]
                            u1=x-0.15*x
                            print(color.LIGHT_PURPLE+"\nThe amount for your product is:",u1)
                        if(a==2):
                            x2=i[3]
                            u2=x2-0.15*x2
                            print(color.LIGHT_PURPLE+"\nThe amount for your product is:",u2)
                        if(a==3):
                            x3=i[-1]
                            u3=x3-0.15*x3
                            print(color.LIGHT_PURPLE+"\nThe amount for your product is:"+color.END,u3)         
            print(color.LIGHT_CYAN+"\nSelect the mode of payment:\n1:Cash\n2:Online payment\n3:EMI"+color.END)
            c=int(input("\nEnter your preference:"))
            if(c==1):
                print(color.BROWN+color.BOLD+color.UNDERLINE+"\n\nYOUR ORDER IS PLACED")
                print("THANK YOU FOR VISITING OUR STORE")
            if(c==2):
                print("\n\nYOUR ORDER IS PLACED")
                print("THANK YOU FOR VISITING OUR STORE"+color.END)
            if(c==3):
                print(color.GREEN+"\nPick you preference: \n1:6 months instalment\n2:8 months instalment"+color.END)
                b=int(input("Enter your preference:"))
                if(b==1):
                    if(a==1):
                        g=u1//6
                        print(color.BLACK+"\nYour monthly payment is",g)
                    if(a==2):
                        f=u2//6
                        print("\nYour monthly payment is",f)
                    if(a==3):
                        t=u3//6
                        print("\nYour monthly payment is",t)
                        
                if(b==2):
                    if(a==1):
                        g=u1//8
                        print("\nYour monthly payment is",g)
                    if(a==2):
                        f=u2//8
                        print("\nYour monthly payment is",f)
                    if(a==3):
                        t=u3//8
                        print("\nYour monthly payment is:"+color.END,t)
                        
            #BILLING
            bil='select max(bill_no) from billing;'
            cur.execute(bil)
            data7=cur.fetchone()
            x=data7[0]
            bill=x+1
            z4="insert into billing values('{}','{}','{}','{}',{});".format(name,idd,e,today,bill)
            cur.execute(z4)
            con.commit()
            
            #insaurance
            if(currentmonth in (1,3,5,7,8,10,12)):
                if(currentmonth in (1,8)):
                    if(day==1):
                        c1=currentmonth-1
                        y1=year+1
                        d1=31
                        i1=date(y1,c1,d1)
                        print(color.PURPLE+"YOUR PRODUCT'S WARRANTY IS VALID TILL-",i1)
                        Z0="insert into validity values('{}',{},'{}');".format(e,bill,i1)
                        cur.execute(Z0)
                        con.commit()
                elif(day==1):
                    d1=30
                    c1=currentmonth-1
                    y1=year+1
                    i2=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i2)
                    Z0="insert into validity values('{}',{},'{}');".format(e,bill,i2)
                    cur.execute(Z0)
                    con.commit()
                else:
                    c1=currentmonth-1
                    y1=year+1
                    d1=day-1
                    i5=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i5)
                    Z0="insert into validity values('{}',{},'{}');".format(e,bill,i5)
                    cur.execute(Z0)
                    con.commit()
                if((year+1)%4==0):
                    if(currentmonth==3):
                        if(day==1):
                            d1=29
                            c1=currentmonth-1
                            y1=year+1
                            i3=date(y1,c1,d1)
                            print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i3)
                            Z0="insert into validity values('{}',{},'{}');".format(e,bill,i3)
                            cur.execute(Z0)
                            con.commit()

                else:
                    if(currentmonth==3):
                        d1=28
                        c1=currentmonth-1
                        y1=year+1
                        i4=date(y1,c1,d1)
                        print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i4)
                        Z0="insert into validity values('{}',{},'{}');".format(e,bill,i4)
                        cur.execute(Z0)
                        con.commit()
            else:
                if(day==1):
                    c1=currentmonth-1
                    y1=year+1
                    d1=31
                    i6=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-",i6)
                    Z0="insert into validity values('{}',{},'{}');".format(e,bill,i6)
                    cur.execute(Z0)
                    con.commit()
                    
                else:
                    c1=currentmonth-1
                    y1=year+1
                    d1=day-1
                    i7=date(y1,c1,d1)
                    print("YOUR PRODUCT'S WARRANTY IS VALID TILL-"+color.END,i7)
                    Z0="insert into validity values('{}',{},'{}');".format(e,bill,i7)
                    cur.execute(Z0)
                    con.commit()
                        
                        
            print(color.YELLOW+color.UNDERLINE+color.BOLD+"\t\t\n\nTHANKS FOR VISITING OUR STORE\nHOPE YOU HAD A GREAT EXPERIENCE\n"+color.END)
            #receipt
            os.system('cls')
            print(color.PURPLE_HIGHLIGHT+color.BOLD+color.ITALIC+'\t\tAPPLE STORE\t\t\t'+color.END)
            print('\tADDRESS:17/46A subhash nagar , new delhi')
            print('\t\tTelp:11223345')
            print('************************************************')
            print('\t\tCASH RECEIPT')
            print('************************************************')
            print('Description')
            print('\nNAME\t     =\t',name)
            print('PHONE NUMBER =\t',idd)
            print('PRODUCT      =\t',e)
            print('BILL NUMBER  =\t',bill,'\n')
            print('__________________________________________________')
            input()
            t="select * from items where model_name='{}';".format(e)
            cur.execute(t)
            con.commit()
            ft=cur.fetchone()
            n=ft[3]
            N=n-1
            n=N
            s="update items set quantity={} where model_name='{}';".format(N,e)
            cur.execute(s)
            con.commit()
        
        else:
            q2="select * from accessories;"
            cur.execute(q2)
            data2=cur.fetchall()
            
            print(color.LIGHT_BLUE+"PLEASE SELECT THE COLOR YOU WANT:")
            u=input("ENTER THE COLOR:")
            for i in data2:
                for j in i:
                    if(j==e):
                        if(i[2]==u):
                            z=i[3]
                            h=z-0.08*z
                            print("THE PRICE OF YOUR PRODUCT IS:",h)                       
            print(color.LIGHT_CYAN+"\nSelect the mode of payment:\n1:Cash\n2:Online payment\n3:EMI"+color.END)
            d=int(input("\nEnter your preference:"))
            if(d==1):
                print(color.BROWN+color.BOLD+color.UNDERLINE+"\n\nYOUR ORDER IS PLACED")
                print("THANK YOU FOR VISITING OUR STORE")
            if(d==2):
                print("\n\nYOUR ORDER IS PLACED")
                print("THANK YOU FOR VISITING OUR STORE"+color.END)
            if(d==3):
                print(color.GREEN+"\nPick you preference: \n1:6 months instalment\n2:8 months instalment"+color.END)
                y=int(input("Enter your preference:"))
                if(y==1):
                    q=h//6
                    print("\nYOUR MONTHLY INSTALLMENT IS-",q)
                    print("THANK YOU FOR VISITING OUR STORE")
                if(y==2):
                    w=h//8
                    print("\nYOUR MONTHLY INSTALLMENT IS-",w)
                    print("THANK YOU FOR VISITING OUR STORE")
                    
            #BILLING
            bil='select max(bill_no) from billing;'
            cur.execute(bil)
            data3=cur.fetchone()
            x=data3[0]
            bill=x+1
            z1="insert into billing values('{}','{}','{}','{}',{});".format(name,idd,e,today,bill)
            cur.execute(z1)
            con.commit()
            
            #insaurance
            if(currentmonth in (1,3,5,7,8,10,12)):
                if(currentmonth in (1,8)):
                    if(day==1):
                        c1=currentmonth-1
                        y1=year+2
                        d1=31
                        i1=date(y1,c1,d1)
                        print(color.LIGHT_GRAY+"\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i1)
                        z0="insert into validity values('{}',{},'{}');".format(e,bill,i1)
                        cur.execute(z0)
                        con.commit()
         
                elif(day==1):
                    d1=30
                    c1=currentmonth-1
                    y1=year+2
                    i2=date(y1,c1,d1)
                    print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i2)
                    z0="insert into validity values('{}',{},'{}');".format(e,bill,i2)
                    cur.execute(z0)
                    con.commit()
         
                else:
                    c1=currentmonth-1
                    y1=year+2
                    d1=day-1
                    i5=date(y1,c1,d1)
                    print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i5)
                    z8="insert into validity values('{}',{},'{}');".format(e,bill,i5)
                    cur.execute(z8)
                    con.commit()
         
                if((year+1)%4==0):
                    if(currentmonth==3):
                        if(day==1):
                            d1=29
                            c1=currentmonth-1
                            y1=year+2
                            i3=date(y1,c1,d1)
                            print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i3)
                            z0="insert into validity values('{}',{},'{}');".format(e,bill,i3)
                            cur.execute(z0)
                            con.commit()
         

                else:
                    if(currentmonth==3):
                        d1=28
                        c1=currentmonth-1
                        y1=year+2
                        i4=date(y1,c1,d1)
                        print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i4)
                        z0="insert into validity values('{}',{},'{}');".format(e,bill,i4)
                        cur.execute(z0)
                        con.commit()
         
            else:
                if(day==1):
                    c1=currentmonth-1
                    y1=year+2
                    d1=31
                    i6=date(y1,c1,d1)
                    print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-\n",i6)
                    z0="insert into validity values('{}',{},'{}');".format(e,bill,i6)
                    cur.execute(z0)
                    con.commit()
                else:
                    c1=currentmonth-1
                    y1=year+2
                    d1=day-1
                    i7=date(y1,c1,d1)
                    print("\nYOUR PRODUCT'S WARRANTY IS VALID TILL-"+color.END,i7,'\n')
                    z0="insert into validity values('{}',{},'{}');".format(e,bill,i7)
                    cur.execute(z0)
                    con.commit()
         
            #receipt
            os.system('cls')
            print(color.PURPLE_HIGHLIGHT+color.BOLD+color.ITALIC+'\t\tAPPLE STORE\t\t\t'+color.END)
            print('\tADDRESS:17/46A subhash nagar , new delhi')
            print('\t\tTelp:11223345')
            print('************************************************')
            print('\t\tCASH RECEIPT')
            print('************************************************')
            print('Description\t\t\tPRICE')
            print('\nNAME\t     =\t',name)
            print('PHONE NUMBER =\t',idd)
            print('PRODUCT      =\t',e,'\t',h)
            print('BILL NUMBER  =\t',bill,'\n')
            print('__________________________________________________')
            input()
            t="select * from items where model_name='{}';".format(r)
            cur.execute(t)
            con.commit()
            ft=cur.fetchone()
            n=ft[3]
            N=n+1
            n=N
            s="update items set quantity={} where model_name='{}';".format(N,k)
            cur.execute(s)
            con.commit()
        again()    
    print(color.LIGHT_BLUE_HIGHLIGHT+'\t\t\tTHE END\t\t\t'+color.END)
    print("\n\n")
    con.close()
again()
