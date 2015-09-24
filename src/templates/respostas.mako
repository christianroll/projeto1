## Saídas de cada máquina
<div id="respostas">
    % for m in maquinas:
        % if m.get('respostas'):
            % for r in m.get('respostas'):
                <div class="resposta"><pre>${r}</pre></div>
            % endfor
        % else:
            <p>${m.get('ip')} não respondeu</p>
        % endif
    % endfor
</div>
