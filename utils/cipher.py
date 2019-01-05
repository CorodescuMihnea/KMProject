class Cypher:
    '''
    '''
    MODE_CBC = 'cbc'
    MODE_CFB = 'cfb'
    MODE_OFB = 'ofb'
    def __init__(self):
        self.text = None
        self.key = None
        #default to cbc
        self.mode = Cypher.CBC

    def encrypt(self, text, key, mode):
        '''
        '''
    def decrypt(self, text, key, mode):
        '''
        '''