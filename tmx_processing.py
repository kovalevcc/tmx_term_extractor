from translate.storage.tmx import tmxfile
import simalign
from keybert import KeyBERT

def get_text(file):
    source = []
    target = []
    with open(file, 'rb') as fin:
        tmx_file = tmxfile(fin, 'en', 'ru')
        for node in tmx_file.unit_iter():
            source.append(node.source)
            target.append(node.target)
        return (' '.join(source).replace("\n", ""), ' '.join(target).replace("\n", ""))

def get_keywords(text):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text)
    return keywords

