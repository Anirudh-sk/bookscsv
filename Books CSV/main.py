from flask import Flask, render_template,url_for,redirect,request, flash
import csv
import random
app = Flask(__name__)
app.secret_key = 'varssha'

adminu='admin'
adminp='password'
useru='user'
userp='password'

nested_dict = { 'Gone_Girl': {'ID': '1','count':'5'},'Forever': {'ID': '2','count':'5'},'Tale of two cities': {'ID': '3','count':'5'},'Two_states': {'ID': '4','count':'5'}}


@app.route('/')
def index():
    return render_template('first.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin', methods=['POST','GET'])
def adminlogin():
   if request.method=='POST':
        email= request.form['login-email']
        password= request.form['login-password']
        if email==adminu and password==adminp:
            return redirect(url_for('dashboard')) 
        else :
            flash('Username or password does not match')
            return redirect(url_for('adminlogin'))

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')

@app.route('/dashboard', methods=['POST'])
def addbook():
   if request.method =='POST':
       title= request.form['title']
       author= request.form['author']
       ID= f'{title}_{author}_{random.randrange(100)}'
       count= request.form['count']
       with open('books.csv', mode='w') as csv_file:
            fieldnames = ['ID', 'title', 'author', 'count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'ID': ID, 'title': title, 'author': author, 'count':count})
       flash('Book added successfully')
       return redirect(url_for('dashboard'))

@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/user', methods=['POST','GET'])
def userlogin():
   if request.method=='POST':
        email= request.form['login-email']
        password= request.form['login-password']
        if email==useru and password==userp:
            return redirect(url_for('dashboard1'))

        else :
            flash('Username or password does not match')
            return redirect(url_for('userlogin'))

@app.route('/dashboard1')
def dashboard1():
    with open('books.csv', mode='r') as csv_file:
        csv_reader =csv.reader(csv_file, delimiter=',')
        line_count = 0
        Title=[]
        Author=[]
        count=[]
        ID=[]
        for row in csv_reader:
            while line_count>1:
                Author.append(row[0])
                Title.append(row[3])
                count.append(row[0])
                ID.append(row[0])
                line_count += 1
        print(Title,Author)
    return render_template('dashboard1.html', Title=Title, Author=Author, count=count,ID=ID)

@app.route('/dashboard1', methods=['POST'])
def returnborrow():
   if request.method=='POST':
       ID=request.form['ID']
       if request.form['return']=='return':
           count=count+1
       else:
           count=count-1


if __name__ == '__main__':
  app.run(debug=True)
 