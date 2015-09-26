<!DOCTYPE html>
<html lang="pt-BR">

    <head>
    <%block name="head">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Projeto 1-Redes de Computadores</title>
        <link rel="shortcut icon" href="" type="image/x-icon" />

        <%block name="stylesheet">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        </%block>

        <%block name="scripts">
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        </%block>
    </%block>
    </head>

    <body>

        <%block name="header">
        <header>
            <h1 class="text-center">
                <%block name="title"/>
            </h1>
        </header>
        </%block>

        <div class="container-fluid">
        <%block name="content">
        </%block>
        </div>
        

        <%block name="footer">
        <footer>
        <%include file="footer.mako"/>
        </footer>
        </%block>

    </body>
</html>
