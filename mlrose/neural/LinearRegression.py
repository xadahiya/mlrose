""" Classes for defining neural network weight optimization problems."""

# Author: Genevieve Hayes (modified by Andrew Rollings)
# License: BSD 3 clause

from sklearn.base import RegressorMixin


from mlrose.algorithms.decay import GeomDecay
from ._NNCore import _NNCore


class LinearRegression(_NNCore, RegressorMixin):
    """Class for defining linear regression weights optimization
    problem. Inherits :code:`fit` and :code:`predict` methods from
    :code:`NeuralNetwork()` class.

    Parameters
    ----------
    algorithm: string, default: 'random_hill_climb'
        Algorithm used to find optimal network weights. Must be one
        of:'random_hill_climb', 'simulated_annealing', 'genetic_alg' or
        'gradient_descent'.

    max_iters: int, default: 100
        Maximum number of iterations used to fit the weights.

    bias: bool, default: True
        Whether to include a bias term.

    learning_rate: float, default: 0.1
        Learning rate for gradient descent or step size for randomized
        optimization algorithms.

    early_stopping: bool, default: False
        Whether to terminate algorithm early if the loss is not improving.
        If :code:`True`, then stop after max_attempts iters with no
        improvement.

    clip_max: float, default: 1e+10
        Used to limit weights to the range [-1*clip_max, clip_max].

    restarts: int, default: 0
        Number of random restarts.
        Only required if :code:`algorithm = 'random_hill_climb'`.

    schedule: schedule object, default = mlrose.GeomDecay()
        Schedule used to determine the value of the temperature parameter.
        Only required if :code:`algorithm = 'simulated_annealing'`.

    pop_size: int, default: 200
        Size of population. Only required if :code:`algorithm = 'genetic_alg'`.

    mutation_prob: float, default: 0.1
        Probability of a mutation at each element of the state vector during
        reproduction, expressed as a value between 0 and 1. Only required if
        :code:`algorithm = 'genetic_alg'`.

    max_attempts: int, default: 10
        Maximum number of attempts to find a better state. Only required if
        :code:`early_stopping = True`.

    random_state: int, default: None
        If random_state is a positive integer, random_state is the seed used
        by np.random.seed(); otherwise, the random seed is not set.

    curve: bool, default: False
        If bool is true, curve containing the fitness at each training
        iteration is returned.

    Attributes
    ----------
    fitted_weights: array
        Numpy array giving the fitted weights when :code:`fit` is performed.

    loss: float
        Value of loss function for fitted weights when :code:`fit` is
        performed.

    fitness_curve: array
        Numpy array giving the fitness at each training iteration.
    """

    def __init__(self, algorithm='random_hill_climb', max_iters=100, bias=True,
                 learning_rate=0.1, early_stopping=False, clip_max=1e+10,
                 restarts=0, schedule=GeomDecay(), pop_size=200,
                 mutation_prob=0.1, max_attempts=10, random_state=None,
                 curve=False):
        _NNCore.__init__(
            self, hidden_nodes=[], activation='identity',
            algorithm=algorithm, max_iters=max_iters, bias=bias,
            is_classifier=False, learning_rate=learning_rate,
            early_stopping=early_stopping, clip_max=clip_max,
            restarts=restarts, schedule=schedule, pop_size=pop_size,
            mutation_prob=mutation_prob, max_attempts=max_attempts,
            random_state=random_state, curve=curve)
