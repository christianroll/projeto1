## Saídas de cada máquina
<div id="respostas">
    % for m in maquinas:
        % if m.get('resposta'):
            <pre>${m.get('resposta')}</pre>
        % else:
            <p>${m.get('ip')} não respondeu</p>
        % endif
    % endfor
</div>
