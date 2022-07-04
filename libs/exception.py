class ElementMissingException(Exception):
    """Can't find element """

    def __init__(self, message):
        super().__init__(message)
