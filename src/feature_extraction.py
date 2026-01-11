from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    max_features=12000,
    ngram_range=(1, 2),          # 🔥 unigrams + bigrams
    stop_words="english",
    sublinear_tf=True            # professional TF scaling
)

def extract_features(texts):
    return vectorizer.fit_transform(texts)

def transform_features(texts):
    return vectorizer.transform(texts)
