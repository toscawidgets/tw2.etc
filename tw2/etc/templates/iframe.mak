<%namespace name="tw" module="tw2.core.mako_util"/>\
% if w.title:
<h1>${w.title}</h1>
% endif
<iframe ${tw.attrs(attrs=w.attrs)}>
<p>Your browser does not support iframes.</p>
</iframe>
