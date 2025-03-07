class BinaryConverter:
    """ Utility class for converting text to binary. """
    #----------------------------------------------------------------
    @staticmethod
    def to_binary(text):
        """Convert string to binary"""
        return ' '.join(format(ord(c), '08b') for c in text)
