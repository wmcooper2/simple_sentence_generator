valid_bigrams = [
        # "I like cats."
        ('PRP','VBP'), ('VBP','NNS'), ('NNS','.'),  # I like cats.
        ('PRP','VBZ'), ('VBZ','NN'), ('NN','.'),  # He likes cats.
        ('WP','VBZ'), ('VBZ','NN'), ('NN','.'),  # Who likes cats.
        ('NNP','VBZ'), ('VBZ','NN'), ('NN','.'),  # David likes cats.

        # "I am a coconut."
        ('PRP', 'VBP'), ('VBP', 'DT'), ('DT', 'NN'), ('NN', '.'),
        ]
