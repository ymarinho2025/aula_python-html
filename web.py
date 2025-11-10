import webbrowser

# Exemplo de HTML no Python
from IPython.display import HTML

html_code = '''

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Meu Perfil</title>

</head>

<body style="font-family: 'Arial', sans-serif; background-color: #f8f8f8; margin: 0; padding: 0;">

 

    <header style="text-align: center; background-color: #3498db; color: #fff; padding: 20px;">

        <h1 style="margin: 0;">Yuri João Marinho</h1>

        <p style="margin: 5px 0;">DEV Full-Stack</p>

    </header>

 

    <section style="margin: 20px; text-align: center;">

        <img src="yuri.jpg" 
        alt="Yuri João Marinho" 
        style="border-radius: 50%; width: 180px; height: 180px; object-fit: cover; margin-bottom: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.3);">



        <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">

            <p>Cidade: Alvorada </p>

            <p>País: Brasil</p>

            <p>Interesses: Web Development, Programação, etc.</p>

        </div>

    </section>

 

    <section style="margin: 20px; text-align: center;">

        <h2>Habilidades</h2>

        <ul style="list-style: none; padding: 0;">

            <li>Linguagens: Python, HTML, CSS, JavaScript</li>

            <li>Ferramentas: Git, VS Code</li>

        </ul>

    </section>

 

    <section style="margin: 20px; text-align: center;">

        <h2>Projeto Recente</h2>

        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>

    </section>

 

    <footer style="text-align: center; margin-top: 20px;">

        <a href="https://www.linkedin.com/in/ymarinho2025/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">LinkedIn</a>

    </footer>

</body>

</html>

''' 

# Exibindo a página HTML
HTML(html_code)

# Salva o arquivo HTML
with open("pagina.html", "w", encoding="utf-8") as f:
    f.write(html_code)

# Abre automaticamente no navegador padrão
webbrowser.open("pagina.html")

print("✅ Página gerada e aberta com sucesso!")