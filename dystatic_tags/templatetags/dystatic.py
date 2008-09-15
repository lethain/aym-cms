from django import template
from django.utils import safestring

try:
    import markdown
except ImportError:
    print u"Requires Markdown library to use Markdown tag."

try:
    import pygments
    from pygments import lexers
    from pygments import formatters
except ImportError:
    print u"Requires Pygments library to use syntax highlighting tags."

register = template.Library()

@register.tag(name="markdown")
def markdownParser(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    parser.delete_first_token()
    return MarkdownNode(nodelist)

class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return markdown.markdown(output)


@register.tag(name="syntax")
def syntaxHighlightParser(parser, token):
    token_list = token.split_contents()
    if len(token_list) > 1:
        lexer = token_list[1]
    else:
        lexer = None

    nodelist = parser.parse(('endsyntax',))
    parser.delete_first_token()
    return SyntaxHighlightNode(nodelist,lexer)

def get_lexer(value,arg):
    if arg is None:
        return lexers.guess_lexer(value)
    return lexers.get_lexer_by_name(arg)

class SyntaxHighlightNode(template.Node):
    def __init__(self, nodelist, lexer):
        self.nodelist = nodelist
        self.lexer = lexer

    def render(self, context):
        output = self.nodelist.render(context)
        lexer = get_lexer(output, self.lexer)
        formatter = formatters.HtmlFormatter()
        h = pygments.highlight(output, lexer, formatter)
        return safestring.mark_safe(h)
        
        
