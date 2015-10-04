<p>Marque os comandos que devem ser enviados a cada máquina</p>
<form class="well" name="comandos" method="post" action="webserver.py">

    % for m in maquinas:
        <label>Máquina ${loop.index + 1} (${m.get('ip')}): </label>
        %for cmd in comandos:
        <label class="checkbox-inline"><input type="checkbox" name="${m.get('ip')}" value="${cmd}">${comandos.get(cmd)}</label>
        <input type="text" name="${m.get('ip')}_arg${cmd}" maxlength="256" pattern="[^|;<>&]+">
        % endfor
        <br>
    % endfor

    <button type="submit" class="btn btn-primary" name="Enviar">Enviar</button>
</form>
