# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReadingConcept(Model):
    """Concept for a critique.

    :param id: ID of the concept, used as a pointer to a particular element in
     ReadingResponse.
    :type id: str
    :param score: Score (confidence) of this concept (reference). We may have
     multiple concepts for the same span of text, hence the score.
    :type score: float
    """

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'score': {'key': 'Score', 'type': 'float'},
    }

    def __init__(self, id=None, score=None):
        super(ReadingConcept, self).__init__()
        self.id = id
        self.score = score
