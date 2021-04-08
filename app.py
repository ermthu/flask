from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from flask import url_for, request, redirect
from flask_mail import Mail,Message
from random import randint

app=Flask(__name__)
mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='exoticdocument@gmail.com'
app.config['MAIL_PASSWORD']='ExoBala@2020'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)








app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "student"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

# =================staff login ==========================================
@app.route('/stafflogin')
def stafflogin():
    return render_template("stafflogin.html")


# =======================================================================
# ===============login page============================================
@app.route('/')
def login():
    return render_template("login.html")

# login users functions
@app.route('/loginuser', methods=['POST', 'GET'])
def loginuser():
    con = mysql.connection.cursor()
    if request.method == 'POST' and "username" in request.form and "password" in request.form:
        username = request.form['username']
        password = request.form['password']
        con.execute("select * from login where  username = %s and password = %s", (username, password))
        res = con.fetchall()
    if res:
        for i in res:
            return render_template("home.html")
    else:
        mess = {"error": "INVALID USER"}
        return render_template("login.html", message=mess)

# =========================staff login functions===========================================
@app.route('/staffuser', methods=['POST', 'GET'])
def staffuser():
    con = mysql.connection.cursor()
    if request.method == 'POST' and "username" in request.form and "password" in request.form:
        username = request.form['username']
        password = request.form['password']
        con.execute("select * from login where  username = %s and password = %s", (username, password))
        res = con.fetchall()
    if res:
        for i in res:
            return render_template("staffdetails.html")
    else:
        mess = {"error": "INVALID USER"}
        return render_template("stafflogin.html", message=mess)
# ========================================================================================
@app.route('/forget',methods=['POST', 'GET'])
def forget():
    if request.method == "POST":
        email = request.form['email']
        msg = Message(subject='OTP', sender='exoticdocument@gmail.com', recipients=[email])
        msg.body = str(otp)
        mail.send(msg)
        return redirect(url_for("forgetpassword"))
    return render_template("forget.html")
# ============================forget function ===========================================


@app.route('/forgetpassword',methods=['POST','GET'])
def forgetpassword():
    return render_template("forgetpassword.html")

# =================================forget valitate password=====================
@app.route('/validate',methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return render_template("sucess.html")
    return render_template("sucess.html")
# ===================================================================================
@app.route('/staffsignup')
def staffsignup():
    return render_template("staffsignup.html")

@app.route('/staffsignupregister',methods=['POST'])
def staffsignupregister():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        con = mysql.connection.cursor()
        sql = "insert into login (username,password) value(%s,%s)"
        con.execute(sql, [name, pwd])
        mysql.connection.commit()
        con.close()
        return render_template("stafflogin.html")





# ==================================================================
@app.route('/n')
def home():
    return render_template("home.html")


@app.route('/home')
def index():
    con = mysql.connection.cursor()
    sql = "select * from entry"
    con.execute(sql)
    res = con.fetchall()

    return render_template("index.html", datas=res)


# delete users
@app.route('/deleteuser/<string:id>', methods=['GET', 'POST'])
def deleteuser(id):
    con = mysql.connection.cursor()
    sql = "delete from entry where ID=%s"
    con.execute(sql, id)
    mysql.connection.commit()
    con.close()

    return redirect(url_for('index'))


# edit users
@app.route('/edituser/<string:id>', methods=['GET', 'POST'])
def edituser(id):
    if request.method == 'POST':
        roll = request.form['roll']
        name = request.form['name']
        father = request.form['father']
        age = request.form['age']
        section = request.form['sec']
        address = request.form['address']
        mobile = request.form['mobile']
        con = mysql.connection.cursor()
        sql = "update entry set ROLL_NUMBER=%s,NAME=%s,FATHER_NAME=%s,AGE=%s,SECTION=%s,ADDRESS=%s,MOBILE_NUMBER=%s where ID= %s"
        con.execute(sql, [roll, name, father, age, section, address, mobile, id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("index"))
    con = mysql.connection.cursor()

    sql = "select * from entry where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()

    return render_template("edituser.html", datas=res)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['user']
        pwd = request.form['passw']
        con = mysql.connection.cursor()
        sql = "insert into login (username,password) value(%s,%s)"
        con.execute(sql, [name, pwd])
        mysql.connection.commit()
        con.close()

        return redirect(url_for('login'))
    return render_template("signup.html")


# add user
@app.route('/addusers', methods=['GET', 'POST'])
def addusers():
    if request.method == 'POST':
        roll = request.form['roll']
        name = request.form['name']
        father = request.form['father']
        age = request.form['age']
        section = request.form['sec']
        address = request.form['address']
        mobile = request.form['mobile']
        con = mysql.connection.cursor()
        sql = "insert into entry(ROLL_NUMBER,NAME,FATHER_NAME,AGE,SECTION,ADDRESS,MOBILE_NUMBER) value(%s,%s,%s,%s,%s,%s,%s)"
        con.execute(sql, [roll, name, father, age, section, address, mobile])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("index"))

    return render_template("addusers.html")


if (__name__ == '__main__'):
    app.run(debug=True)

