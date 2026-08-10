from flask import Flask, request, url_for
from datetime import datetime
from html import escape

app = Flask(__name__)


# =========================================================
# SEUS DADOS
# =========================================================

NOME = "Cláudio Gustavo Lopes de Andrade"
PRONTUARIO = "PT303741x"
INSTITUICAO = "IFSP"


# Momento em que a aplicação foi carregada
ultima_atualizacao = datetime.now()


# =========================================================
# LAYOUT DO SITE
# =========================================================

def pagina(conteudo):

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>Avaliação contínua - Aula 040</title>

        <style>

            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                padding: 0;

                font-family:
                    Arial,
                    Helvetica,
                    sans-serif;

                background-color: white;
                color: #222;
            }}


            /* ============================
               MENU SUPERIOR
            ============================ */

            .navbar {{
                width: 100%;
                height: 55px;

                background-color: #222;

                border-top:
                    4px solid #1b2740;
            }}


            .navbar-container {{

                width: 1080px;
                max-width: 90%;

                height: 51px;

                margin: auto;

                display: flex;
                align-items: center;

                gap: 30px;
            }}


            .titulo-menu {{

                color: #aaa;

                font-size: 18px;

                margin-right: 5px;
            }}


            .titulo-menu strong {{

                color: #aaa;
            }}


            .navbar a {{

                text-decoration: none;

                color: #aaa;

                font-size: 14px;

                transition: 0.2s;
            }}


            .navbar a:hover {{

                color: white;
            }}



            /* ============================
               CONTEÚDO
            ============================ */

            .container {{

                width: 1080px;

                max-width: 90%;

                margin:
                    55px
                    auto
                    0
                    auto;
            }}


            h1 {{

                margin: 0;

                font-size: 35px;

                font-weight: 400;

                color: #222;
            }}


            hr {{

                margin:
                    18px
                    0
                    20px
                    0;

                border: 0;

                border-top:
                    1px solid #e5e5e5;
            }}


            p {{

                margin:
                    0
                    0
                    14px
                    0;

                font-size: 14px;

                line-height: 1.4;
            }}


            .texto-grande {{

                font-size: 29px;

                margin-bottom: 16px;

                line-height: 1.2;
            }}



            /* ============================
               RESPONSIVO
            ============================ */

            @media (max-width: 700px) {{

                .navbar {{
                    height: auto;
                }}


                .navbar-container {{

                    height: auto;

                    padding:
                        15px
                        0;

                    flex-direction: column;

                    align-items: flex-start;

                    gap: 12px;
                }}


                .container {{

                    margin-top: 35px;
                }}


                h1 {{

                    font-size: 28px;
                }}


                .texto-grande {{

                    font-size: 21px;
                }}

            }}

        </style>

    </head>


    <body>


        <!-- MENU -->

        <nav class="navbar">

            <div class="navbar-container">


                <span class="titulo-menu">

                    Avaliação contínua:
                    <strong>Aula 040</strong>

                </span>


                <a href="{url_for('home')}">

                    Home

                </a>


                <a href="{url_for(
                    'identificacao',
                    nome=NOME,
                    prontuario=PRONTUARIO,
                    instituicao=INSTITUICAO
                )}">

                    Identificação

                </a>


                <a href="{url_for('contexto')}">

                    Contexto da requisição

                </a>


            </div>

        </nav>



        <!-- CONTEÚDO -->

        <main class="container">

            {conteudo}

        </main>


    </body>

    </html>
    """


# =========================================================
# CALCULA QUANTO TEMPO PASSOU
# =========================================================

def tempo_passado():

    agora = datetime.now()

    diferenca = agora - ultima_atualizacao

    segundos = int(
        diferenca.total_seconds()
    )


    if segundos < 60:

        return "That was a few seconds ago."


    minutos = segundos // 60


    if minutos == 1:

        return "That was a minute ago."


    if minutos < 60:

        return f"That was {minutos} minutes ago."


    horas = minutos // 60


    if horas == 1:

        return "That was an hour ago."


    return f"That was {horas} hours ago."


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    data = ultima_atualizacao


    meses = [

        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

    ]


    mes = meses[data.month]


    hora = data.strftime(
        "%I:%M %p"
    ).lstrip("0")


    data_formatada = (

        f"{mes} "
        f"{data.day}, "
        f"{data.year} "
        f"{hora}"

    )


    conteudo = f"""

        <h1>
            Dados da última atualização:
        </h1>


        <hr>


        <p>

            The local date and time is
            {data_formatada}.

        </p>


        <p>

            {tempo_passado()}

        </p>

    """


    return pagina(conteudo)


# =========================================================
# IDENTIFICAÇÃO
# =========================================================

@app.route(
    "/user/<nome>/<prontuario>/<instituicao>"
)
def identificacao(
    nome,
    prontuario,
    instituicao
):

    nome = escape(nome)
    prontuario = escape(prontuario)
    instituicao = escape(instituicao)


    conteudo = f"""

        <h1>

            Olá, {nome}!

        </h1>


        <hr>


        <p class="texto-grande">

            Prontuário: {prontuario}

        </p>


        <p class="texto-grande">

            Instituição: {instituicao}

        </p>

    """


    return pagina(conteudo)


# =========================================================
# CONTEXTO DA REQUISIÇÃO
# =========================================================

@app.route("/contexto")
def contexto():

    navegador = escape(
        request.headers.get(
            "User-Agent",
            "Não identificado"
        )
    )


    ip = escape(
        request.remote_addr
        or
        "Não identificado"
    )


    host = escape(
        request.host
    )


    conteudo = f"""

        <h1>

            Olá, {escape(NOME)}!

        </h1>


        <hr>


        <p class="texto-grande">

            Seu navegador é:
            {navegador}

        </p>


        <p class="texto-grande">

            O IP do computador remoto é:
            {ip}

        </p>


        <p class="texto-grande">

            O host da aplicação é:
            {host}

        </p>

    """


    return pagina(conteudo)