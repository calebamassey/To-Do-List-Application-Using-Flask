from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todo_list.append(todo)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
