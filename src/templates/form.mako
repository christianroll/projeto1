<p>Marque os comandos que devem ser enviados a cada máquina</p>
<form class="well" name="comandos" method="post" action="webserver.py">

    % for m in maquinas:
        <label>Máquina ${loop.index} (${m.get('ip')}): </label>
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="1">ps</label>
        <input type="text" name="${m.get('ip')}_arg1" maxlength="256" pattern="[^|;<>&]+">

        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="2">df</label>
        <input type="text" name="${m.get('ip')}_arg2" maxlength="256" pattern="[^|;<>&]+">

        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="3">finger</label>
        <input type="text" name="${m.get('ip')}_arg3" maxlength="256" pattern="[^|;<>&]+">

        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="4">uptime</label>
        <input type="text" name="${m.get('ip')}_arg4" maxlength="256" pattern="[^|;<>&]+">
        <br>
    % endfor

    <button type="submit" class="btn btn-primary" name="Enviar">Enviar</button>
</form>
