from fileinput import filename
from flask import Flask, render_template, url_for,request,redirect

app = Flask(__name__)
print(__name__)# is __main__ because this is main file we are running

#How to make these writing routes dynamic???

@app.route('/')
def my_home():# thats defaults
    return render_template('index.html')
    
@app.route('/<string:page_name>')  # we want page name which should be of type string
def html_page(page_name):   #give page_name as param
    return render_template(page_name)

# just creting function to write to txt
def write_to_text:
    with open('infostore.txt', 'a') as f:
        text = request.form['text']
        processed_text = text.upper()
        message = request.form['message']
        f.write(str(form[message])

@app.route('/submit_form', methods =['POST', 'GET'])
def submit_form():
    message = request.form['message']
    email = request.form['email']
    if request.method == 'POST':
        data = request.form.to_dict() #['email']['message'] we are grabbing data in dict
        print(data)
        return render_template('thankyou.html')
    else:
        return 'oops try again sth is wrong'

if __name__ == '__main__':  
   app.run(debug = True)  