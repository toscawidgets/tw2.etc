import tw2.core as twc

class IFrameWidget(twc.Widget):
    template = "tw2.etc.templates.iframe"
    title = twc.Param("Title (optional)", default=None)
    height = twc.Param(default='100%', attribute=True)
    width = twc.Param(default='100%', attribute=True)
    src = twc.Param("Source for the iframe", attribute=True)
