class EncoderDecoderType(object):

    def is_type(self, obj):
        """ Defines if object is to be encoded/decoded by this type
        
        Args:
            obj: instance to test against 
        
        Returns:
            True if type can handle instance, False otherwise
        """
        raise NotImplementedError

    def encode(self, obj):
        """ Provides encoding for given instance 
        
        Args:
            obj: instance to encode 
        """
        raise NotImplementedError

    def decode(self, obj):
        """ Provides decoding for given instance 

        Args:
            obj: instance to decode 
        """
        raise NotImplementedError
