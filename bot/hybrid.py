from chatterbot.comparisons import Comparator
import spacy


class HybridSimilarity(Comparator):
    def __init__(self, language="en_core_web_md"):
        super().__init__(language)
        self.nlp = spacy.load(language)

    def compare(self, statement, other_statement):
        # Get spaCy docs
        doc1 = self.nlp(statement.text.lower())
        doc2 = self.nlp(other_statement.text.lower())

        # Semantic similarity using spaCy vectors
        semantic_sim = doc1.similarity(doc2)

        # Token overlap (Jaccard similarity)
        tokens1 = set(
            [token.lemma_ for token in doc1 if not token.is_stop and not token.is_punct]
        )
        tokens2 = set(
            [token.lemma_ for token in doc2 if not token.is_stop and not token.is_punct]
        )

        if len(tokens1) == 0 or len(tokens2) == 0:
            token_sim = 0
        else:
            intersection = len(tokens1 & tokens2)
            union = len(tokens1 | tokens2)
            token_sim = intersection / union if union > 0 else 0

        # Weighted combination
        combined_score = (0.7 * semantic_sim) + (0.3 * token_sim)

        return combined_score
