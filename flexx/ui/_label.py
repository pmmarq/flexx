
from .. import react
from . import Widget


class Label(Widget):
    """ Widget to show text/html.
    
    Example:
    
    .. UIExample:: 100
        
        from flexx import ui
        
        class App(ui.App):
            def init(self):
                self.b1 = ui.Label(text='This is a label')
    
    """
    
    CSS = ".flx-label { border: 0px solid #454; }"

    @react.input
    def text(v=''):
        """ The text on the label.
        """
        # todo: use react.check_str() or something?
        if not isinstance(v, str):
            raise ValueError('Text input must be a string.')
        return v
    
    class JS:
        
        def _js_create_node(self):
            # todo: allow setting a placeholder DOM element, or any widget parent
            this.node = document.createElement('div')
            #this.node.className = this.cssClassName
            flexx.get('body').appendChild(this.node);
            # this.node.innerHTML = 'a label'
            # super()._init()
        
        @react.connect('text')
        def _text_changed(self, text):
            this.node.innerHTML = text