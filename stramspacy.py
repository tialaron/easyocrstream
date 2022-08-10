import spacy_streamlit

models = ["en_core_web_sm", "/path/to/model"]
default_text = "Sundar Pichai is the CEO of Google."
visualizers = ["ner", "textcat"]
spacy_streamlit.visualize(models, default_text, visualizers)