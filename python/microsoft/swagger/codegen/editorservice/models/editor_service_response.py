from msrest.serialization import Model


class EditorServiceResponse(Model):

    analyzer_name = ''
    matches = 0
    editor_score = 0

    def __init__(self, name, score, errors):
        self.analyzer_name = name
        self.matches = errors
        self.editor_score = score
