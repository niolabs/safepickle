class EncoderDecoderType(object):

    def encoder_type(self, obj):
        raise NotImplementedError

    def encode(self, obj):
        raise NotImplementedError

    def decoder_type(self, obj):
        raise NotImplementedError

    def decode(self, obj):
        raise NotImplementedError
