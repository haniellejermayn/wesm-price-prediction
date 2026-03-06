import torch
import torch.nn as nn
import torch.nn.init


class NeuralNetwork(nn.Module):

    def __init__(self,
                 input_size,
                 num_classes,
                 list_hidden,
                 activation='relu'):
        
        """Class constructor for NeuralNetwork"""
        super(NeuralNetwork, self).__init__()

        self.input_size = input_size
        self.num_classes = num_classes
        self.list_hidden = list_hidden
        self.activation = activation

    def create_network(self):

        """Creates the layers of the neural network."""
        layers = []

        # first layer
        layers.append(nn.Linear(self.input_size, self.list_hidden[0]))

        # activation function
        layers.append(self.get_activation(self.activation))

        # iterate through hidden layers
        for i in range(len(self.list_hidden) - 1):

            layers.append(nn.Linear(self.list_hidden[i], self.list_hidden[i + 1]))

            layers.append(self.get_activation(self.activation))

        # last layer
        layers.append(nn.Linear(self.list_hidden[-1], self.num_classes))
        
        #remove since we are doing regression
        # layers.append(nn.Softmax(dim=1))
        
        self.layers = nn.Sequential(*layers)

    def init_weights(self):

        """Initializes the weights of the network."""
        torch.manual_seed(2)

        # For each layer in the network
        for module in self.modules():

            # If it is a torch.nn.Linear layer
            if isinstance(module, nn.Linear):

                # initialize weights
                nn.init.normal_(module.weight, mean=0, std=0.1)

                # initialize bias terms
                nn.init.constant_(module.bias, 0)

    def get_activation(self,
                       mode='relu'):
        
        """Returns the torch.nn layer for the activation function."""
        activation = nn.ReLU(inplace=True)

        if mode == 'tanh':
            activation = nn.Tanh()

        elif mode == 'relu':
            activation = nn.ReLU(inplace=True)

        return activation

    def forward_manual(self,
                       x,
                       verbose=False):
        """Forward propagation of the model, implemented manually."""

        # For each layer in the network
        for i in range(len(self.layers) - 1):

            # If it is a torch.nn.Linear layer
            if isinstance(self.layers[i], nn.Linear):

                # TODO: Compute the result of the linear layer. Do not forget
                # to add the bias term. Assign the result to x.
                # HINT: Use torch.matmul() function.
                weight = self.layers[i].weight
                bias = self.layers[i].bias

                x = torch.matmul(x, weight.t()) + bias

            # If it is another function
            else:
                # Call the forward() function of the layer
                # and return the result to x.
                x = self.layers[i](x)

            if verbose:
                # Print the output of the layer
                print('Output of layer ' + str(i))
                print(x, '\n')

        # Apply the softmax function
        probabilities = self.layers[-1](x)

        if verbose:
            print('Output of layer ' + str(len(self.layers) - 1))
            print(probabilities, '\n')

        return x, probabilities

    def forward(self,
                x,
                verbose=False):
        """Forward propagation of the model, implemented using PyTorch."""

        # For each layer in the network
        for i in range(len(self.layers) - 1):

            # Call the forward() function of the layer
            # and return the result to x.
            x = self.layers[i](x)

            if verbose:
                # Print the output of the layer
                print('Output of layer ' + str(i))
                print(x, '\n')

        # Apply the softmax function
        probabilities = self.layers[-1](x)

        if verbose:
            print('Output of layer ' + str(len(self.layers) - 1))
            print(probabilities, '\n')

        return x, probabilities

    def predict(self,
                probabilities):
        """Returns the index of the class with the highest probability."""

        return torch.argmax(probabilities, dim=1)
