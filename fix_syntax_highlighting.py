import sublime
import sublime_plugin


class DockerfileSyntax:

    SYNTAX_FILE = 'Packages/Dockerfile Syntax Highlighting/Syntaxes/Dockerfile.sublime-syntax'

    @staticmethod
    def is_my_file(filename):
        return filename.endswith('.Dockerfile') or filename.endswith('/Dockerfile')


class NginxSyntax:

    SYNTAX_FILE = 'Packages/nginx/Syntaxes/nginx.sublime-syntax'

    @staticmethod
    def is_my_file(filename):
        return filename.endswith('nginx.conf')


SYNTAXES = (
    DockerfileSyntax,
    NginxSyntax,
)


def syntax_exists(package_based_path):
    """Check if syntax file exists.

    :type package_based_path: str
    :param package_based_path: syntax file specified in Sublime Text's
                               packages format.

    .. note::
        Sublime Text specifies syntax file path in format::

            Packages/Python/Python.sublime-syntax
            Packages/User/Python-custom.sublime-syntax

    """

    try:
        sublime.load_binary_resource(package_based_path)
        return True
    except OSError:
        return False


class FixSyntaxHighlighterEventListener(sublime_plugin.EventListener):

    def on_load_async(self, view):
        filename = view.file_name()

        if filename:
            for syntax in SYNTAXES:
                if syntax.is_my_file(filename):
                    if syntax_exists(syntax.SYNTAX_FILE):
                        view.set_syntax_file(syntax.SYNTAX_FILE)
                        break
