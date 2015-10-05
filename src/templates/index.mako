<%inherit file="base.mako"/>

<%block name="header">
    ${parent.header()}
</%block>

<%block name="title">
    Projeto 1 - Redes de Computadores
</%block>

<%block name="content">
    <%include file="form.mako"/>

    %if respostas:
        <%include file="respostas.mako"/>
    %endif

    %if DEBUG:
        <div id="debug">
            <h2>DEBUG</h2>
            ${DEBUG}
        </div>
    %endif

</%block>
