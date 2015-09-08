<p>Marque os comandos que devem ser enviados a cada máquina</p>
<form class="well" name="comandos" method="post" action="webserver.py">

    % for m in maquinas:
        <label>Máquina ${loop.index} (${m.get('ip')}): </label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="ps">ps</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="df">df</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="finger">finger</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="uptime">uptime</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="rm" disabled>rm -rf /</label>
        <br>
    % endfor

    <button type="submit" class="btn btn-primary" name="Enviar">Enviar</button>
</form>
