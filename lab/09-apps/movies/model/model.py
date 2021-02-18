import pickle
import logging
from pathlib import Path
from pkg_resources import resource_filename

class Sentiment(object):
    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.base_path = Path(resource_filename(__name__, '.'))
        self.model_path = self.base_path / 'imdb'
        self._load_pkl_and_setattr('imdb_tfidf.pkl', 'tfidf')
        self._load_pkl_and_setattr('imdb_mlp.pkl', 'mlp')

    def _load_pkl_and_setattr(self, pkl_file, attribute_name):
        try:
            pkl_file_path = self.model_path / pkl_file
            with open(pkl_file_path, 'rb') as f:
                data = pickle.load(f)
                setattr(self, attribute_name, data)
        except Exception as e:
            logging.critical("load pkf file [%s] failed with Exception:", pkl_file)
            logging.critical(e, exc_info=True)

    def predict(self, text):
        if not isinstance(text, str):
            raise TypeError(f'type of parameter \'text\' in method \'predict\' must be \'str\' and not \'{type(text)}\'')
       
        X = self.tfidf.transform([text])
        probability = self.mlp.predict_proba(X).item(1)
        classification = 1 if probability > self.threshold else 0

        result = {
            "probability"    : probability,
            "classification" : classification
        }
        return result

if __name__ == '__main__':
    s = Sentiment()
    result = s.predict("The movie was so good")
    print(result)


