class ListWordBuilder:
    """ build list of words from string in order to send them in ES query """
    @staticmethod
    def get_list_of_pairs(self,words):
        list_of_pairs = [s for s in words if ' ' in s]
        return list_of_pairs


    @staticmethod
    def get_list_of_single_words(self,words):
        list_of_single_words = [s for s in words if ' ' not in s]
        return list_of_single_words

