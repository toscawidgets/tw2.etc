from tw2.etc.widgets import *
from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest

class TestIFrameWidget(WidgetTest):
    widget = IFrameWidget
    attrs = {'url' : 'foo'}
    expected = """
<div>
<iframe src="foo" height="100%" width="100%">
<p>Your browser does not support iframes.</p>
</iframe>
</div>"""
