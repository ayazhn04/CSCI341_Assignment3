from flask import Flask,render_template,request,redirect,url_for,flash
import psycopg2
import psycopg2.extras

app=Flask(__name__)
app.secret_key='my_secret_key_123'

db_host="localhost"
db_name="caregivers_db"
db_user="postgres"
db_pass="Uam12072004!"

def get_db():
    con=psycopg2.connect(host=db_host,database=db_name,user=db_user,password=db_pass)
    return con

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def show_users():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM app_user ORDER BY user_id")
    all_users=cur.fetchall()
    con.close()
    return render_template('users.html',users=all_users)

@app.route('/users/new',methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        email=request.form['email']
        fname=request.form['given_name']
        lname=request.form['surname']
        city=request.form['city']
        phone=request.form['phone_number']
        desc=request.form['profile_description']
        pwd=request.form['password']

        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO app_user (email,given_name,surname,city,phone_number,profile_description,password) VALUES (%s,%s,%s,%s,%s,%s,%s)",(email,fname,lname,city,phone,desc,pwd))
            con.commit()
            flash('New user added!','success')
            return redirect(url_for('show_users'))
        except Exception as e:
            con.rollback()
            flash(f'Something went wrong: {e}','danger')
        finally:
            con.close()
    return render_template('users_form.html',user=None)

@app.route('/users/<int:id>/edit',methods=['GET','POST'])
def edit_user(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        email=request.form['email']
        fname=request.form['given_name']
        lname=request.form['surname']
        city=request.form['city']
        phone=request.form['phone_number']
        desc=request.form['profile_description']
        pwd=request.form['password']
        try:
            cur.execute("UPDATE app_user SET email=%s,given_name=%s,surname=%s,city=%s,phone_number=%s,profile_description=%s,password=%s WHERE user_id=%s",(email,fname,lname,city,phone,desc,pwd,id))
            con.commit()
            flash('User updated!','success')
            return redirect(url_for('show_users'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM app_user WHERE user_id=%s",(id,))
    user_data=cur.fetchone()
    con.close()
    return render_template('users_form.html',user=user_data)

@app.route('/users/<int:id>/delete',methods=['POST'])
def delete_user(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM app_user WHERE user_id=%s",(id,))
        con.commit()
        flash('User deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Could not delete user: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_users'))

@app.route('/caregivers')
def show_caregivers():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    c_type=request.args.get('type')
    c_city=request.args.get('city')
    sql="SELECT c.*,u.given_name,u.surname,u.city FROM caregiver c JOIN app_user u ON c.caregiver_user_id=u.user_id WHERE 1=1"
    args=[]
    if c_type:
        sql+=" AND c.caregiving_type ILIKE %s"
        args.append(f'%{c_type}%')
    if c_city:
        sql+=" AND u.city ILIKE %s"
        args.append(f'%{c_city}%')
    sql+=" ORDER BY c.caregiver_user_id"
    cur.execute(sql,args)
    caregivers_list=cur.fetchall()
    con.close()
    return render_template('caregivers.html',caregivers=caregivers_list)

@app.route('/caregivers/new',methods=['GET','POST'])
def add_caregiver():
    if request.method=='POST':
        uid=request.form['caregiver_user_id']
        pic=request.form['photo']
        gen=request.form['gender']
        ctype=request.form['caregiving_type']
        rate=request.form['hourly_rate']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO caregiver (caregiver_user_id,photo,gender,caregiving_type,hourly_rate) VALUES (%s,%s,%s,%s,%s)",(uid,pic,gen,ctype,rate))
            con.commit()
            flash('Caregiver added!','success')
            return redirect(url_for('show_caregivers'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('caregivers_form.html',caregiver=None)

@app.route('/caregivers/<int:id>/edit',methods=['GET','POST'])
def edit_caregiver(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        pic=request.form['photo']
        gen=request.form['gender']
        ctype=request.form['caregiving_type']
        rate=request.form['hourly_rate']
        try:
            cur.execute("UPDATE caregiver SET photo=%s,gender=%s,caregiving_type=%s,hourly_rate=%s WHERE caregiver_user_id=%s",(pic,gen,ctype,rate,id))
            con.commit()
            flash('Caregiver updated!','success')
            return redirect(url_for('show_caregivers'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM caregiver WHERE caregiver_user_id=%s",(id,))
    data=cur.fetchone()
    con.close()
    return render_template('caregivers_form.html',caregiver=data)

@app.route('/caregivers/<int:id>/delete',methods=['POST'])
def delete_caregiver(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM caregiver WHERE caregiver_user_id=%s",(id,))
        con.commit()
        flash('Caregiver deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_caregivers'))

@app.route('/members')
def show_members():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT m.*,u.given_name,u.surname,u.city FROM member m JOIN app_user u ON m.member_user_id=u.user_id ORDER BY m.member_user_id")
    members_list=cur.fetchall()
    con.close()
    return render_template('members.html',members=members_list)

@app.route('/members/new',methods=['GET','POST'])
def add_member():
    if request.method=='POST':
        uid=request.form['member_user_id']
        rules=request.form['house_rules']
        desc=request.form['dependent_description']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO member (member_user_id,house_rules,dependent_description) VALUES (%s,%s,%s)",(uid,rules,desc))
            con.commit()
            flash('Member added!','success')
            return redirect(url_for('show_members'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('members_form.html',member=None)

@app.route('/members/<int:id>/edit',methods=['GET','POST'])
def edit_member(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        rules=request.form['house_rules']
        desc=request.form['dependent_description']
        try:
            cur.execute("UPDATE member SET house_rules=%s,dependent_description=%s WHERE member_user_id=%s",(rules,desc,id))
            con.commit()
            flash('Member updated!','success')
            return redirect(url_for('show_members'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM member WHERE member_user_id=%s",(id,))
    data=cur.fetchone()
    con.close()
    return render_template('members_form.html',member=data)

@app.route('/members/<int:id>/delete',methods=['POST'])
def delete_member(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM member WHERE member_user_id=%s",(id,))
        con.commit()
        flash('Member deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_members'))

@app.route('/addresses')
def show_addresses():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT a.*,u.given_name,u.surname FROM address a JOIN member m ON a.member_user_id=m.member_user_id JOIN app_user u ON m.member_user_id=u.user_id ORDER BY a.member_user_id")
    addr_list=cur.fetchall()
    con.close()
    return render_template('addresses.html',addresses=addr_list)

@app.route('/addresses/new',methods=['GET','POST'])
def add_address():
    if request.method=='POST':
        uid=request.form['member_user_id']
        num=request.form['house_number']
        st=request.form['street']
        town=request.form['town']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO address (member_user_id,house_number,street,town) VALUES (%s,%s,%s,%s)",(uid,num,st,town))
            con.commit()
            flash('Address added!','success')
            return redirect(url_for('show_addresses'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('addresses_form.html',address=None)

@app.route('/addresses/<int:id>/edit',methods=['GET','POST'])
def edit_address(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        num=request.form['house_number']
        st=request.form['street']
        town=request.form['town']
        try:
            cur.execute("UPDATE address SET house_number=%s,street=%s,town=%s WHERE member_user_id=%s",(num,st,town,id))
            con.commit()
            flash('Address updated!','success')
            return redirect(url_for('show_addresses'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM address WHERE member_user_id=%s",(id,))
    data=cur.fetchone()
    con.close()
    return render_template('addresses_form.html',address=data)

@app.route('/addresses/<int:id>/delete',methods=['POST'])
def delete_address(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM address WHERE member_user_id=%s",(id,))
        con.commit()
        flash('Address deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_addresses'))

@app.route('/jobs')
def show_jobs():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT j.*,u.given_name,u.surname FROM job j JOIN member m ON j.member_user_id=m.member_user_id JOIN app_user u ON m.member_user_id=u.user_id ORDER BY j.job_id")
    jobs_list=cur.fetchall()
    con.close()
    return render_template('jobs.html',jobs=jobs_list)

@app.route('/jobs/new',methods=['GET','POST'])
def add_job():
    if request.method=='POST':
        uid=request.form['member_user_id']
        req_type=request.form['required_caregiving_type']
        other=request.form['other_requirements']
        posted=request.form['date_posted']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO job (member_user_id,required_caregiving_type,other_requirements,date_posted) VALUES (%s,%s,%s,%s)",(uid,req_type,other,posted))
            con.commit()
            flash('Job posted!','success')
            return redirect(url_for('show_jobs'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('jobs_form.html',job=None)

@app.route('/jobs/<int:id>/edit',methods=['GET','POST'])
def edit_job(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        req_type=request.form['required_caregiving_type']
        other=request.form['other_requirements']
        posted=request.form['date_posted']
        try:
            cur.execute("UPDATE job SET required_caregiving_type=%s,other_requirements=%s,date_posted=%s WHERE job_id=%s",(req_type,other,posted,id))
            con.commit()
            flash('Job updated!','success')
            return redirect(url_for('show_jobs'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM job WHERE job_id=%s",(id,))
    data=cur.fetchone()
    con.close()
    return render_template('jobs_form.html',job=data)

@app.route('/jobs/<int:id>/delete',methods=['POST'])
def delete_job(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM job WHERE job_id=%s",(id,))
        con.commit()
        flash('Job deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_jobs'))

@app.route('/jobs/<int:id>/applicants')
def show_job_applicants(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT c.*,u.given_name,u.surname,ja.date_applied FROM job_application ja JOIN caregiver c ON ja.caregiver_user_id=c.caregiver_user_id JOIN app_user u ON c.caregiver_user_id=u.user_id WHERE ja.job_id=%s",(id,))
    applicants_list=cur.fetchall()
    con.close()
    return render_template('job_applicants_list.html',applicants=applicants_list,job_id=id)

@app.route('/job_applications')
def show_applications():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM job_application ORDER BY date_applied DESC")
    apps=cur.fetchall()
    con.close()
    return render_template('job_applications.html',applications=apps)

@app.route('/job_applications/new',methods=['GET','POST'])
def add_application():
    if request.method=='POST':
        cid=request.form['caregiver_user_id']
        jid=request.form['job_id']
        date=request.form['date_applied']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO job_application (caregiver_user_id,job_id,date_applied) VALUES (%s,%s,%s)",(cid,jid,date))
            con.commit()
            flash('Applied successfully!','success')
            return redirect(url_for('show_applications'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('job_applications_form.html')

@app.route('/job_applications/<int:caregiver_id>/<int:job_id>/delete',methods=['POST'])
def delete_application(caregiver_id,job_id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM job_application WHERE caregiver_user_id=%s AND job_id=%s",(caregiver_id,job_id))
        con.commit()
        flash('Application removed.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_applications'))

@app.route('/appointments')
def show_appointments():
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT a.*,c_user.given_name as caregiver_name,c_user.surname as caregiver_surname,m_user.given_name as member_name,m_user.surname as member_surname FROM appointment a JOIN caregiver c ON a.caregiver_user_id=c.caregiver_user_id JOIN app_user c_user ON c.caregiver_user_id=c_user.user_id JOIN member m ON a.member_user_id=m.member_user_id JOIN app_user m_user ON m.member_user_id=m_user.user_id ORDER BY a.appointment_date DESC,a.appointment_time DESC")
    appts=cur.fetchall()
    con.close()
    return render_template('appointments.html',appointments=appts)

@app.route('/appointments/new',methods=['GET','POST'])
def add_appointment():
    if request.method=='POST':
        cid=request.form['caregiver_user_id']
        mid=request.form['member_user_id']
        date=request.form['appointment_date']
        time=request.form['appointment_time']
        hours=request.form['work_hours']
        status=request.form['status']
        con=get_db()
        cur=con.cursor()
        try:
            cur.execute("INSERT INTO appointment (caregiver_user_id,member_user_id,appointment_date,appointment_time,work_hours,status) VALUES (%s,%s,%s,%s,%s,%s)",(cid,mid,date,time,hours,status))
            con.commit()
            flash('Appointment created!','success')
            return redirect(url_for('show_appointments'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    return render_template('appointments_form.html',appointment=None)

@app.route('/appointments/<int:id>/edit',methods=['GET','POST'])
def edit_appointment(id):
    con=get_db()
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=='POST':
        cid=request.form['caregiver_user_id']
        mid=request.form['member_user_id']
        date=request.form['appointment_date']
        time=request.form['appointment_time']
        hours=request.form['work_hours']
        status=request.form['status']
        try:
            cur.execute("UPDATE appointment SET caregiver_user_id=%s,member_user_id=%s,appointment_date=%s,appointment_time=%s,work_hours=%s,status=%s WHERE appointment_id=%s",(cid,mid,date,time,hours,status,id))
            con.commit()
            flash('Appointment updated!','success')
            return redirect(url_for('show_appointments'))
        except Exception as e:
            con.rollback()
            flash(f'Error: {e}','danger')
        finally:
            con.close()
    cur.execute("SELECT * FROM appointment WHERE appointment_id=%s",(id,))
    data=cur.fetchone()
    con.close()
    return render_template('appointments_form.html',appointment=data)

@app.route('/appointments/<int:id>/confirm',methods=['POST'])
def confirm_appointment(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("UPDATE appointment SET status='accepted' WHERE appointment_id=%s",(id,))
        con.commit()
        flash('Confirmed!','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_appointments'))

@app.route('/appointments/<int:id>/delete',methods=['POST'])
def delete_appointment(id):
    con=get_db()
    cur=con.cursor()
    try:
        cur.execute("DELETE FROM appointment WHERE appointment_id=%s",(id,))
        con.commit()
        flash('Appointment deleted.','success')
    except Exception as e:
        con.rollback()
        flash(f'Error: {e}','danger')
    finally:
        con.close()
    return redirect(url_for('show_appointments'))

if __name__=="__main__":
    app.run(debug=True)
