import numpy as np


class DataLoader(object):

    def __init__(self, X, y, batch_size):
        """Class constructor for DataLoader"""
        self.X = X
        self.y = y
        self.batch_size = batch_size

        self.indices = np.array([i for i in range(self.X.shape[0])])
        np.random.seed(1)

    def shuffle(self):
        """Shuffles the indices in self.indices."""

        np.random.shuffle(self.indices)

    def get_batch(self, mode='train'):
        """Returns self.X and self.y divided into different batches of size
        self.batch_size according to the shuffled self.indices."""

        X_batch = []
        y_batch = []

        # If mode is set to `train`, shuffle the indices first using
        if mode == 'train':
            self.shuffle()
        elif mode == 'test':
            self.indices = np.array([i for i in range(self.X.shape[0])])

        # The loop that will iterate from 0 to the number of instances with
        # step equal to self.batch_size
        for i in range(0, len(self.indices), self.batch_size):

            # Check if we can still get self.batch_size from the
            # remaining indices starting from index i. Edit the condition
            # below.
            if i + self.batch_size <= len(self.indices):
                indices = self.indices[i:i + self.batch_size]

            # Else, just get the remaining indices from index i until the
            # last element in the list. Edit the statement inside the else
            # block.
            else:
                indices = self.indices[i:]

            X_batch.append(self.X[indices])
            y_batch.append(self.y[indices])

        return X_batch, y_batch
