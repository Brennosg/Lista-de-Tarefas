# Importa os módulos Flask, render_template, request, redirect e url_for do pacote flask
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)  

todos = [
    {
        'id': 1,
        'name': 'Write SQL',
        'checked': False  # Esta tarefa ainda não está marcada como concluída
    },
    {
        'id': 2,
        'name': 'Write Python',
        'checked': True # Esta tarefa está marcada como concluída
    }
]
# Define as rotas ("/"), ("/home")
@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if (request.method == "POST"):
        todo_name = request.form["todo_name"]
        cur_id = random.randint(1, 1000)
        todos.append(
            {
            'id': cur_id,
            'name': todo_name,
            'checked': False
            }
        )
        return redirect(url_for("home")) # Redireciona para a página inicial depois de adicionar a tarefa
    return render_template("index.html", items=todos)

@app.route("/checked/<int:todo_id>", methods=["POST"]) # Define a rota para marcare desmarcar uma tarefa como concluída
def checked_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked']  
            break
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>", methods=["POST"]) # Define a rota para deletar uma tarefa
def delete_todo(todo_id):
    global todos
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True) # Executa a aplicação Flask em modo debug