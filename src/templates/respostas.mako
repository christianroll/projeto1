## Saídas de cada máquina
<div id="respostas">
    % for m in maquinas:
        % if m.get('respostas'):
            % for r in m.get('respostas'):
                <div class="resposta">
                    <h2 class="cmd">${r[0]}</h2>
                    <pre>${r[1]}</pre>
                </div>
            % endfor
        % else:
            <p>${m.get('ip')} não respondeu</p>
        % endif
    % endfor
</div>
