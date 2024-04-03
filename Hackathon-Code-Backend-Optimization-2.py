import mysql.connector as a
con= a.connect(host="localhost",user="root",password="1234",database="societies",auth_plugin='mysql_native_password')
if con.is_connected():
    print("Successfully connected.")
else:
    print("Something went wrong.")

c= con.cursor(buffered= True)
from tabulate import tabulate

c.execute("show tables")
# To see tables
def show_tables():
    for display in c:
        print(tabulate(display))
    print("="*150)
    main()


# To see amc officers details.
def amc_officers_details():
    a= "select*from amcofficers"
    c= con.cursor()
    c.execute(a)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['a_id','a_email_id','a_name','phone_no','address','position','a_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# To add,update,delete amc officers details.
def amc_add():
    a_id= input("Enter amc officer id: ")
    a_email_id= input("Enter email address: ")
    a_name= input("Enter name: ")
    phone_no= int(input("Enter phone number: "))
    address= input("Enter address: ")
    position= input("Enter position: ")
    a_login_id= input("Enter a_login_id: ")
    pswd= input("Enter pswd: ")
    data= (a_id,a_email_id,a_name,phone_no,address,position,a_login_id,pswd)
    sql= 'insert into amcofficers values(%s,%s,%s,%s,%s,%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

def amc_updation():
    a_id= input("Enter amc officer id: ")
    sql= 'select*from amcofficers'
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['a_id','a_email_id','a_name','phone_no','address','position','a_login_id','pswd'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==a_id:
            ch= input("To change amc member's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change amc member's email_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new email_id: ")
            ch= input("To change amc member's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new name: ")
            ch= input("To change amc member's phone_no  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new phone: ")
            ch= input("To change amc member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter new address: ")
            ch= input("To change amc member's position press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter position: ")
            ch= input("To change amc member's login_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[6]= input("Enter new login_id: ")
            ch= input("To change amc member's pswd press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[7]= input("Enter new pswd: ")
            sql1= 'update amcofficers set a_id= %s, a_email_id= %s, a_name= %s, phone_no= %s, address= %s, position= %s, a_login_id= %s, pswd= %s where a_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break
        
def amc_delete():
    a_id= input("Enter a_id: ")
    a_name= input("Enter a_name: ")
    data= (a_id,a_name)
    sql= 'delete from amcofficers where a_id= %s and a_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

def amc_check():
    sql= 'select*from amcofficers'
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['a_id','a_email_id','a_name','phone_no','address','position','a_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()

def amc_operations():
    choice= input("Enter 1. Add  2. Update  3. Delete 4. Check")
    if(choice=='1'):
        amc_add()
    elif(choice=='2'):
        amc_updation()
    elif(choice=='3'):
        amc_delete()
    elif(choice=='4'):
        amc_check()
    else:
        main()
    
# To add, update, delete management table.
# To add in a particular management table.
def add1():
    table_name= input("Enter table name: ")
    m_id= input("Enter the id of the member in management: ")
    m_email_id= input("Enter email id of the member in management: ")
    m_name= input("Enter name of the member in management: ")
    phone_no= input("Enter phone number of the member in management: ")
    address= input("Enter address of society member: ")
    role= input("Enter the position of the member in management: ")
    m_login_id= input("Enter login_id of the member in management: ")
    pswd= input("Enter password of the member in management: ")
    data= (m_id,m_email_id,m_name,phone_no,address,role,m_login_id,pswd)
    sql= 'insert into '+table_name+' values(%s,%s,%s,%s,%s,%s,%s,%s)'
    con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

#To check management table.
def check1():
    table_name= input("Enter the name of management table: ")
    sql= 'select*from '+table_name
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['m_id','m_email_id','m_name','phone_no','address','role','m_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()
    
# To update in a management table.
def update1():
    table_name= input("Enter table name: ")
    m_id= input("Enter member id: ")
    sql= 'select*from '+table_name
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['m_id','m_email_id','m_name','phone_no','address','role','m_login_id','pswd'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==m_id:
            ch= input("To change management member's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change management member's email_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new email_id: ")
            ch= input("To change management member's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new name: ")
            ch= input("To change management member's phone_no  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new phone: ")
            ch= input("To change management member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter new address: ")
            ch= input("To change management member's role press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter role: ")
            ch= input("To change society member's m_login_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[6]= input("Enter new m_login_id: ")
            ch= input("To change management member's pswd press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[7]= input("Enter new pswd: ")
            sql1= 'update '+table_name+' set m_id= %s, m_email_id= %s, m_name= %s, phone_no= %s, address= %s, role= %s, m_login_id= %s, pswd= %s where m_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break
        
# To delete in a management table.
def delete1():
    table_name= input("Enter management table name: ")
    m_id= input("Enter m_id: ")
    m_name= input("Enter m_name: ")
    data= (m_id,m_name)
    sql= 'delete from '+table_name+' where m_id= %s and m_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()        

def operations_on_particular_management_table():
    choice= input("Tasks:-   1. Add   2. Update   3. Delete   4. Check")
    if (choice=='1'):
        add1()
    elif (choice=='2'):
        update1()
    elif (choice=='3'):
        delete1()
    elif (choice=='4'):
        check1()
    else:
        main()





# To see particular managing table.
def particular_managing_team_details():
    a= input("Enter society id: ")
    b= input("Enter society name: ")
    data= (a,b)
    sql= 'select*from management_list where society_id= %s and s_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','secretary_name','phone_no'],tablefmt='fancy_grid'))
    print("="*150)
    main()

def enter_details_in_management_list():
    society_id= input("Enter society id: ")
    s_name= input("Enter society name: ")
    secretary_name= input("Enter secretary_name: ")
    phone_no= input("Enter society phone number: ")
    data= (society_id,s_name,secretary_name,phone_no)
    sql= 'insert into management_list values(%s,%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

# To see list of management table.
def list_of_management_tables():
    a= "select*from management_list"
    c= con.cursor()
    c.execute(a)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','phone_no','secretary_name'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# To create a particular management table for particular society.
# To create a particular managment team table.
def creating_new_management_team_table():
    management_name= input("Enter managing table name for creating the management table: ")
    new_table= 'create table '+management_name+' like management'
    c= con.cursor()
    c.execute(new_table)
    enter_details_in_management_list()


# To add,update,delete building team details.
#To add.
def building_add():
    b_id= input("Enter the id of the member of building team: ")
    b_email_id= input("Enter email id of the member in building team: ")
    b_name= input("Enter name of the member in building team: ")
    phone_no= input("Enter phone number of the member in building team: ")
    address= input("Enter address of building team member: ")
    expertise= input("Enter the expertise of the member in building team: ")
    b_login_id= input("Enter login_id of the member in building team: ")
    pswd= input("Enter password of the member in building team: ")
    data= (b_id,b_email_id,b_name,phone_no,address,expertise,b_login_id,pswd)
    sql= 'insert into buildingteam values(%s,%s,%s,%s,%s,%s,%s,%s)'
    con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

#To check.
def building_check():
    sql= 'select*from buildingteam'
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['b_id','b_email_id','b_name','phone_no','address','expertise','b_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# To delete from building team table.
def building_delete():
    b_id= input("Enter b_id: ")
    b_name= input("Enter b_name: ")
    data= (b_id,b_name)
    sql= 'delete from buildingteam where b_id= %s and b_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()
 
#To update.
def building_update():
    n_id= input("Enter building team member id: ")
    sql= 'select*from buildingteam'
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['b_id','b_email_id','b_name','phone_no','address','expertise','b_login_id','pswd'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==n_id:
            ch= input("To change building team member's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change society member's email_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new email_id: ")
            ch= input("To change society member's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new name: ")
            ch= input("To change society member's phone_no  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new phone: ")
            ch= input("To change society member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter new address: ")
            ch= input("To change society member's expertise press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter expertise: ")
            ch= input("To change building team member's b_login_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[6]= input("Enter new b_login_id: ")
            ch= input("To change building team member's pswd press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[7]= input("Enter new pswd: ")
            sql1= 'update buildingteam set b_id= %s, b_email_id= %s, b_name= %s, phone_no= %s, address= %s, expertise= %s, b_login_id= %s, pswd= %s where b_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break

#building team operations.
def operations_on_building_team_table():
    choice= input("Tasks:-   1. Add   2. Update   3. Delete   4. Check")
    if (choice=='1'):
        building_add()
    elif (choice=='2'):
        building_update()
    elif (choice=='3'):
        building_delete()
    elif (choice=='4'):
        building_check()
    else:
        main()

# To see building team details.
def building_team_details():
    a= "select*from buildingteam"
    c= con.cursor()
    c.execute(a)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['b_id','b_email_id','b_name','phone_no','address','expertise','b_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()
    
# To see list of societies.
def list_of_societies():
    a= "select*from societylist"
    c= con.cursor()
    c.execute(a)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','zone','address','pincode','phone_no','secretary_name','ownership'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# To check particular society details.
def particular_society_details():
    a= input("Enter society id: ")
    b= input("Enter society name: ")
    data= (a,b)
    sql= 'select*from societylist where society_id= %s and s_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','zone','address','pincode','phone_no','secretary_name','ownership'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# To enter details in society list.
def enter_details_in_society_list():
    society_id= input("Enter society id: ")
    s_name= input("Enter society name: ")
    zone= input("Enter zone of society: ")
    address= input("Enter society address: ")
    pincode= input("Enter pincode: ")
    phone_no= input("Enter society phone number: ")
    secretary_name= input("Enter secretary_name: ")
    ownership= input("Enter society ownership: ")
    data= (society_id,s_name,zone,address,pincode,phone_no,secretary_name,ownership)
    sql= 'insert into societylist values(%s,%s,%s,%s,%s,%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

# To update,delete in societylist.
# To update in a society list table.
def update_society_list():
    society_id= input("Enter society id: ")
    sql= 'select*from societylist'
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','zone','address','pincode','phone_no','secretary_name','ownership'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==society_id:
            ch= input("To change society's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change society's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new society name: ")
            ch= input("To change zone of the society name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new zone for the society: ")
            ch= input("To change society member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new address: ")
            ch= input("To change society's pincode press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter pincode: ")    
            ch= input("To change society's phone_no  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter new phone: ")
            ch= input("To change society's secretary name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[6]= input("Enter new secretary name: ")
            ch= input("To change society member's ownership press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[7]= input("Enter new ownership: ")    
            sql1= 'update societylist set society_id= %s, s_name= %s, zone= %s, address= %s,pincode= %s, phone_no= %s, secretary_name= %s, ownership= %s where society_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break
        
# To delete in a society list table.
def delete_society_list():
    table_name= input("Enter society table name: ")
    society_id= input("Enter society_id: ")
    s_name= input("Enter name: ")
    data= (society_id,s_name)
    sql= 'delete from societylist where society_id= %s and s_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

#To check society list table.
def check_society_list():
    sql= 'select*from societylist'
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','zone','address','pincode','phone_no','secretary_name','ownership'],tablefmt='fancy_grid'))
    print("="*150)
    main()

# operations on society list table.
def operations_on_society_list():
    choice= input("Tasks:- 1. Update   2. Delete   3. Check")
    if (choice=='1'):
        update_society_list()
    elif (choice=='2'):
        delete_society_list()
    elif (choice=='3'):
        check_society_list()
    else:
        main()

# To create a particular society table.
def creating_new_society_table():
    s_name= input("Enter society name for creating the society table: ")
    new_table= 'create table '+s_name+' like per_society_table'
    c= con.cursor()
    c.execute(new_table)
    enter_details_in_society_list()


# To add in a particular society table.
def add():
    table_name= input("Enter society's table name: ")
    table_id= input("Enter society's id: ")
    n_id= input("Enter society member id: ")
    n_email_id= input("Enter society member email id: ")
    name= input("Enter society member name: ")
    phone_no= input("Enter society member's phone number: ")
    address= input("Enter address of society member: ")
    gender= input("Enter gender of society member: ")
    dob= input("Enter birth date of society member: ")
    ownership= input("Enter ownership of society member: ")
    rent_amount= input("Enter rent_amount if society member is leaving on rent: ")
    paid_bills= input("Enter paid bills names: ")
    pending_bills= input("Enter pending bills names: ")
    complaints= input("Enter complaints: ")
    n_login_id= input("Enter login_id of society member: ")
    pswd= input("Enter password of society member: ")
    data= (n_id,n_email_id,name,phone_no,address,gender,dob,ownership,rent_amount,paid_bills,pending_bills,complaints,n_login_id,pswd)
    sql= 'insert into '+table_name+' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

#To check particular society table.
def check():
    table_name= input("Enter society's table name: ")
    table_id= input("Enter society's id: ")
    sql= 'select*from '+table_name
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['n_id','n_email_id','name','phone_no','address','gender','dob','ownership','rent_amount','paid_bills','pendig_bills','complaints','n_login_id','pswd'],tablefmt='fancy_grid'))
    print("="*150)
    main()
    

# To update in a particular society table.
def update():
    table_name= input("Enter society's table name: ")
    n_id= input("Enter member id: ")
    sql= 'select*from '+table_name
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['n_id','n_email_id','name','phone_no','address','gender','dob','ownership','rent_amount','paid_bills','pendig_bills','complaints','n_login_id','pswd'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==n_id:
            ch= input("To change society member's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change society member's email_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new email_id: ")
            ch= input("To change society member's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new name: ")
            ch= input("To change society member's phone_no  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new phone: ")
            ch= input("To change society member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter new address: ")
            ch= input("To change society member's gender press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter gender: ")
            ch= input("To change society member's dob press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[6]= input("Enter new dob: ")
            ch= input("To change society member's ownership press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[7]= input("Enter new ownership: ")
            ch= input("To change society member's rent_amount press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[8]= input("Enter new rent_amount: ")
            ch= input("To change society member's paid_bills press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[9]= input("Enter new paid_bills: ")
            ch= input("To change society member's pending_bills press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[10]= input("Enter new pending_bills: ")
            ch= input("To change society member's complaints press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[11]= input("Enter new complaints: ")
            ch= input("To change society member's n_login_id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[12]= input("Enter new n_login_id: ")
            ch= input("To change society member's pswd press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[13]= input("Enter new pswd: ")
            sql1= 'update '+table_name+' set n_id= %s, n_email_id= %s, name= %s, phone_no= %s, address= %s, gender= %s, dob= %s, ownership= %s, rent_amount= %s, paid_bills= %s, pending_bills= %s, complaints= %s, n_login_id= %s, pswd= %s where n_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break

# To delete in a particular society table.
def delete():
    table_name= input("Enter society table name: ")
    n_id= input("Enter n_id: ")
    name= input("Enter name: ")
    data= (n_id,name)
    sql= 'delete from '+table_name+' where n_id= %s and name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

# To add,update,delete in a particular society table.
def operations_on_particular_society_table():
    choice= input("Tasks:-   1. Add   2. Update   3. Delete   4. Check")
    if (choice=='1'):
        add()
    elif (choice=='2'):
        update()
    elif (choice=='3'):
        delete()
    elif (choice=='4'):
        check()
    else:
        main()

#To display payment list of all payment tables.
def display_payment_tables():
    a= "select*from payment_tables"
    c= con.cursor()
    c.execute(a)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['society_id','s_name','society_payment_table'],tablefmt='fancy_grid'))
    print("="*150)
    main()

#To create list of payment tables for all societies.
def enter_details_in_payment_tables_society_list():
    society_id= input("Enter society id: ")
    s_name= input("Enter society name: ")
    society_payment_table= input("Enter society payment table name: ")
    data= (society_id,s_name,society_payment_table)
    sql= 'insert into payment_tables values(%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()

# To create table for particular payment table for particular society.
def creating_particular_payment_table():
    table_name= input("Enter society_name for creating the payment table for particular society table: ")
    new_table= 'create table '+table_name+' like payment_list'
    c= con.cursor()
    c.execute(new_table)
    enter_details_in_payment_tables_society_list()
    main()
    
# To add in a particular payment table.
def add_payment():
    table_name= input("Enter society's payment table name: ")
    n_id= input("Enter society member id: ")
    n_name= input("Enter society member name: ")
    amt_paid = input("Enter the paid amount: ")
    amt_pending = input("Enter the pending amount: ")
    penalty_amt= input("Enter penalty amount: ")
    address= input("Enter address of society member: ")
    data= (n_id,n_name,amt_paid,amt_pending,penalty_amt,address)
    sql= 'insert into '+table_name+' values(%s,%s,%s,%s,%s,%s)'
    con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()
    
# To update in a payment table.
def update_payment():
    table_name= input("Enter table name: ")
    n_id= input("Enter member id: ")
    sql= 'select*from '+table_name
    c.execute(sql,)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['n_id','n_name','amt_paid','amt_pending','penalty_amt','address'],tablefmt='fancy_grid'))
    for i in myresult:
        i= list(i)
        if i[0]==n_id:
            ch= input("To change member's id press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[0]= input("Enter new id: ")
            ch= input("To change member's name press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[1]= input("Enter new name: ")
            ch= input("To change paid amount  press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[2]= input("Enter new amount: ")
            ch= input("To change pending amount press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[3]= input("Enter new amount: ")
            ch= input("To change penalty amount press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[4]= input("Enter new penalty amount: ")
            ch= input("To change member's address press (Y/N): ")
            if ch=='y' or ch=='Y':
                i[5]= input("Enter new address: ")
            sql1= 'update '+table_name+' set n_id= %s, n_name= %s, amt_paid= %s,amt_pending= %s, penalty_amt = %s, address= %s where n_id= %s'
            value= (i[0],i[1],i[2],i[3],i[4],i[5],i[0])
            c.execute(sql1,value)
            con.commit()
            print("="*150)
            main()
            break

# To delete in a particular paymenttable.
def delete_payment():
    table_name= input("Enter society table name: ")
    n_id= input("Enter n_id: ")
    n_name= input("Enter name: ")
    data= (n_id,n_name)
    sql= 'delete from '+table_name+' where n_id= %s and n_name= %s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("="*150)
    main()
#To check particular payment table.
def check_payment():
    table_name= input("Enter society's payment table name: ")
    sql= 'select*from '+table_name
    c.execute(sql)
    myresult= c.fetchall()
    print(tabulate(myresult,headers=['n_id','n_name','amt_paid','amt_pending','penalty_amt','address'],tablefmt='fancy_grid'))
    print("="*150)
    main()    
# To do operation on payment table
def operations_on_particular_payment_table():
    choice= input("Tasks:-   1. Add   2. Update   3. Delete   4. Check")
    if (choice=='1'):
        add_payment()
    elif (choice=='2'):
        update_payment()
    elif (choice=='3'):
        delete_payment()
    elif (choice=='4'):
        check_payment()
    else:
        main()


# Exit program.
def ending_program():
    exit()


# main function.
def main():
    print("""                                                   *******Tasks*******

              1. To see tables    2.  AMC Officers Details     3. AMC Operations     4. Building Team Details    5. Operations Building Team table
              
    6.List of Societies  7.Particular Society Details  8. Creating new society table  9. Operation on particular society table 10.Operations on society list
    
    11. List of management_teams  12. Particular Management Team Details   13. Creating new managment team table  14.Management Table Operations
    
         15. To create particular payment table for particular society   16.List of payment tables   17.Operations on Payment table   18. Exit     """)
    print("-"*150)
    choice= input("Enter task no.:- ")
    if(choice == '1'):
        show_tables()
    elif(choice == '2'):
        amc_officers_details()
    elif(choice == '3'):
        amc_operations()
    elif(choice == '4'):
        building_team_details()
    elif(choice == '5'):
        operations_on_building_team_table()
    elif(choice == '6'):
        list_of_societies()
    elif(choice == '7'):
        particular_society_details()
    elif(choice == '8'):
        creating_new_society_table()
    elif(choice == '9'):
        operations_on_particular_society_table()
    elif(choice == '10'):
        operations_on_society_list()
    elif(choice == '11'):
        list_of_management_tables()
    elif(choice == '12'):
        particular_managing_team_details()
    elif(choice == '13'):
        creating_new_management_team_table()
    elif(choice == '14'):
        operations_on_particular_management_table()
    elif(choice == '15'):
        creating_particular_payment_table()
    elif(choice == '16'):
        display_payment_tables()
    elif(choice == '17'):
        operations_on_particular_payment_table()
    elif(choice == '18'):
        ending_program()
    else:
        print("_"*150)
        print("                                                                     Wrong Choice                                                          ")
        print("                                                                      Try Again                                                            ")
        print("-"*150)
        main()




def pswd():
    p= input("Password: ")
    if p == "DEV":
        print("_"*150)
        main()
    else:
        print("Wrong Password")
        print("=*"*75)
        pswd()
pswd()
