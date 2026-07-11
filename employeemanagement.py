import mysql.connector as db
con=db.connect(user="root",password="Vishnu@123",host="localhost",database="taskmangement")
cur=con.cursor()
def view_total():
    cur.execute('select * from employee')
    rows=cur.fetchall()
    print('id\tname\trole\tmalil')
    for row in rows:
        print(row)
def view_taks():
    cur.execute('select*from task')
    rows=cur.fetchall()
    print('taskid\ttitle\tdescrition\tpriority\due_date\statuse')
    for row in rows:
        print(row)



while True:
    print('1.admin login')
    print('2.employee login')
    print('3.exit')
    ch=input('enter you choice:')
    if ch=='1':
        pas=input('enter you password:')
        if pas=='1234':
            while True:
                print('1.dashboard')
                print('2.employee management')
                print('3.task management')
                print('4.task monitoring')
                print('5.reports')
                print('6.exit')
                choice=input('enter your ch:')
                if choice=='1':
                    while True:
                        print('1.view total employees')
                        print('2.view total tasks')
                        print('3.status')
                        print('4.exit from dashboard')
                        ch=input('enter your choice:')
                        if ch=='1':
                            '''
                            def view_total():
                                cur.execute('select * from employe')
                                rows=cur.fetchall()
                                print('id\tname\trole\tmalil')
                                for row in rows:
                                    print(row)
                                    '''
                            view_total()
                        elif ch=='2':
                            def total_task():
                                cur.execute('select * from task')
                                rows=cur.fetchall()
                                print('id\ttitle\tdescription\tpriority\tdue_date\tstatuse')
                                for row in rows:
                                    print(row)
                            total_task()
                        elif ch=='3':
                            def task_status():
                                cur.execute('select statuse from task')
                                rows=cur.fetchall()
                                for row in rows:
                                    print(row)
                            task_status()
                        elif ch=='4':
                            break
                elif choice=='2':
                    while True:
                        print('1.add employee')
                        print('2.update details')
                        print('3.delect employee')
                        print('4.view list')
                        ch=input('enter your choice:')
                        if ch=='1':
                            def add_employee():
                                name=input('enter the name:')
                                role=input('enter the role of employee:')
                                email=input('enter the mail:')
                                cur.execute('insert into employee(empname,emprole,email) values(%s,%s,%s)',
                                            ((name,role,email)))
                                con.commit()
                                print('employe added successfully')
                            add_employee()
                        elif ch=='2':
                            def update_employee():
                                name=input('enter the name:')
                                role=input('enter the role')
                                email=input('enter the mail')
                                cur.execute('update employe set empname=%s ,emprole=%s,email=%s',(name,role,email))
                                con.commit()
                                print('updated successfully')
                            update_employee()
                            
                        elif ch=='3':
                            def delete_employee():
                                name=input('enter the name:')
                                cur.execute('delete from employe where empname=%s',[name])
                                con.commit()
                                print('delected successsfully')
                            delete_employee()
                        elif ch=='4':
                            view_total()
                            '''
                            cur.execute('select * from employe')
                            rows=cur.fetchall()
                            print('id\tname\trole\tmalil')
                            for row in rows:
                                print(row)
                                '''
                        else:
                            break
                elif choice=='3':
                    while True:
                        print('1.creat task')
                        print('2.assign a task to employee')
                        print('3.update task details')
                        print('4.delete task')
                        ch=input('enter your choice:')
                        if ch=='1':
                            def create_task():
                                task=input('enter the tasktitle:')
                                description=input('enter the description:')
                                priority=input('enter the priority:')
                                due_date=input('enter the status:')
                                cur.execute('insert into task(title,description,priority,due_date,statuse) values(%s,%s,%s,%s,%s)',
                                            ((task,description,priority,due_date)))
                                con.commit()
                                print('employe added successfully')
                            create_task()
                            
                            
                        elif ch=='2':
                            def assign_task():
                                employeeid=input('enter the employee_id:')
                                taskid=input('enter the task_id:')
                                comments=input('enter the commentes:')
                                cur.execute('insert into assignedtasks set employeeid=%s,taskid=%s,comment=%s',[employeeid,taskid,comments])
                                con.commit()
                                print('assigned successfully')
                            assign_task()
                        elif ch=='3':
                            def update_task():
                                title=input('enter the name:')
                                description=input('enter the role')
                                priority=input('enter the mail')
                                due=input('enter the date:')
                                statuse=input('enter the new status:')
                                cur.execute('update  employe set title=%s ,description=%s,due_date=%s,statuse=%s',
                                            (title,description,priority,due,statuse))
                                con.commit()
                                print('updated successfully')
                            update_task()
                        elif ch=='4':
                            def delete_task():
                                title=input('enter the name:')
                                cur.execute('delete from employe where title=%s',(title))
                                con.commit()
                                print('delected successsfully')
                            delete_task()
                        else:
                            break
                elif choice=='4':
                    while True:
                        print('1.view all tasks')
                        print('2.check task status')
                        print('3.track process')
                        ch=input('enter your choice:')
                        if ch=='1':
                            view_taks()
                        elif ch=='2':
                            def status_check():
                                cur.execute('select statuse from task')
                                rows=cur.fetchall()
                                for row in rows:
                                    print(row)
                            status_check()
                            
                        elif ch=='3':
                            def track():
                                cur.execute('select statuse from task')
                                rows=cur.fetchall()
                                for row in rows:
                                    print(row)
                            track()
                        else:
                            break
                elif choice=='5':
                    while True:
                        print('1.task complete report')
                        print('2.performance')
                        print('3.overdue task report')
                        ch=input('enter your choice:')
                        if ch=='1':
                            view_taks()
                        elif ch=='2':
                            def performance():
                                cur.execute("""
                                select statuse,
                                       case
                                           when statuse='completed' then 'A Good'
                                           when statuse='oartial' then 'B Average'
                                           else 'Need to Improve'
                                       end as performance
                                from task
                                """)
                                rows=cur.fetchall()
                                print("Status\t\tGrade")
                                for row in rows:
                                    print(row)
                            performance()
                            
                        elif ch=='3':
                            def overdue():
                                cur.execute('''select * from task where statuse !='completed' and due_date<curdate()''')
                                rows=cur.fetchall()
                                for row in rows:
                                    print(row)
                            overdue()
                        else:
                            break
                        
                elif choice=='6':
                    break
                else:
                    print('enter the correct choice')
                
        else:
            print('worng password')
    elif ch=='2':
        while True:
            print('1.dashboard')
            print('2.my tasks')
            print('3.task details')
            print('4.update status')
            print('5.commenmts')
            ch=input('enter your choice:')
            if ch=='1':
                def details():
                    empi=input('enter the employee id :')
                    cur.execute('select * from employee where empid=%s',[empi])
                    rows=cur.fetchall()
                    print('id\tname\trole\tmalil')
                    for row in rows:
                        print(row)
                details()
            elif ch=='2':
                def mytask():
                    employee_id=input('enter the employeeid:')
                    cur.execute('select * from assignedtasks a inner join task t on (a.taskid=t.taskid) where a.employeeid=%s',
                                [employee_id])
                    rows=cur.fetchall()
                    print('taskid\title')
                    for row in rows:
                        print(row)
                mytask()
                    
            elif ch=='3':
                def taskdetails():
                    employee_id=input('enter the employeeid:')
                    cur.execute('select *from assignedtasks a inner join task t on (a.taskid=t.taskid) where a.employeeid=%s',
                                [employee_id])
                    rows=cur.fetchall()
                    for row in rows:
                        print(row)
                taskdetails()
            elif ch=='4':
                taskid=input('enter the taskid:')
                status=input('enter the status:')
                cur.execute('update task set statuse=%s where taskid=%s ',(status,taskid))
                con.commit()
                print('updated successfully')
            elif ch=='5':
                def complete():
                    taskid=input('enter the task id:')
                    employeeid=input('enter the employee id :')
                    cur.execute('insert into comment(taskid,employeeid) values(%s,%s)',[taskid,employeeid])
                    con.commit()
                    print('inserted successfully')
                complete()
            else:
                break
            

    elif ch=='3':
        break
cur.close()
con.close()
