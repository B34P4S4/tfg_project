# creamos un índice para los vectores

import numpy as np

class VectorStore:
    def __init__(self, dim=384):
        self.vectors = []
        self.texts = []

    def add(self, embedding, text):
        self.vectors.append(embedding)
        self.texts.append(text)

    def search(self, query_embedding, top_k=2, k=None):
        if k is not None:
            top_k = k
            
        if not self.vectors:
            return []

        similarities = []

        for i, vec in enumerate(self.vectors):
            score = np.dot(query_embedding, vec) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(vec)
            )
            similarities.append((score, self.texts[i]))

        similarities.sort(reverse=True)

        return [text for _, text in similarities[:top_k]]
