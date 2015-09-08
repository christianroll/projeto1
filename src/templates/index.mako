<%inherit file="base.mako"/>

<%block name="header">
    ${parent.header()}
</%block>

<%block name="title">
    Projeto 1
</%block>

<%block name="content">
    <pre>
    M1: ${m1}
    M2: ${m2}
    </pre>
</%block>
