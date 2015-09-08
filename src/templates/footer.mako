<%!
    import datetime
    def getDate():
        return datetime.datetime.now()
%>

<%block name="footer">
<hr>
<p>${getDate()}</p>
<hr>
<div id="license">
</div>

<div class="license" id="licence">
<p>${autores}</p>
</div>
</%block>
