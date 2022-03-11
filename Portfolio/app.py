import email
import csv
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
def write_to_text(data):
    with open('database.txt', mode ='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
        
def write_to_csv(data):
    with open('data.csv', 'a', newline = '') as csv_data:
        email = data['email']
        subject  = data['subject']
        message  = data['message']
        to_csv_writer = csv.writer(csv_data, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        to_csv_writer.writerow([email, subject, message])
        # text = request.form['text']
        # processed_text = text.upper()
        # message = request.form['message']
        # f.write(str(form[message])

@app.route('/submit_form', methods =['POST', 'GET'])
def submit_form():
    message = request.form['message']
    email = request.form['email']
    
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #['email']['message'] we are grabbing data in dict
            print(data) #instead of printing we will call write method and write to text
            write_to_text(data)
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'something is not working, saving failed'
    else:
        return 'oops try again sth is wrong'

if __name__ == '__main__':  
   app.run(debug = True)  