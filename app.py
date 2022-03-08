from flask import Flask,render_template,redirect,url_for

app=Flask(__name__)

@app.route('/')
def alwin():
    return render_template('home.htm')

@app.route('/customer')
def customer():
    return render_template('customer.htm')

@app.route('/admin')
def admin():
    return render_template('admin.htm')


if __name__=='__main__':
    app.run(debug=True)


