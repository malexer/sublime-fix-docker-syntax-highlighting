from collections import OrderedDict, UserDict

import sublime
import sublime_plugin


DOCKERFILE_SYNTAX = 'Packages/Dockerfile Syntax Highlighting/Syntaxes/Dockerfile.sublime-syntax'


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


class FixDockerSyntaxHighlighterEventListener(sublime_plugin.EventListener):

    def on_load_async(self, view):
        filename = view.file_name()

        if filename:
            if filename.endswith('.Dockerfile') or filename.endswith('/Dockerfile'):
                if syntax_exists(DOCKERFILE_SYNTAX):
                    view.set_syntax_file(DOCKERFILE_SYNTAX)
