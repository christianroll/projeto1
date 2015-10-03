<p>Marque os comandos que devem ser enviados a cada máquina</p>
<form class="well" name="comandos" method="post" action="webserver.py">

    % for m in maquinas:
        <label>Máquina ${loop.index} (${m.get('ip')}): </label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="1">ps</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="2">df</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="3">finger</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="4">uptime</label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="rf" disabled>rm -rf /</label>
        <br>
    % endfor

    <button type="submit" class="btn btn-primary" name="Enviar">Enviar</button>
</form>
