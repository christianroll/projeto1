<%inherit file="base.mako"/>

<%block name="header">
    ${parent.header()}
</%block>

<%block name="title">
    Projeto 1
</%block>

<%block name="content">
    <%include file="form.mako"/>
</%block>
