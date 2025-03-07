class BinaryConverter:
#----------------------------------------------------------------

    @staticmethod
    def from_binary(binary_text):
        
        return ''.join(chr(int(b, 2)) for b in binary_text.split())
