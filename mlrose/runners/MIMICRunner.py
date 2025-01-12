import mlrose
from mlrose import short_name
from mlrose.runners._RunnerBase import _RunnerBase

"""
Example usage:

    experiment_name = 'example_experiment'
    problem = TSPGenerator.generate(seed=SEED, number_of_cities=22)

    mmc = MIMICRunner(problem=problem,
                      experiment_name=experiment_name,
                      output_directory=OUTPUT_DIRECTORY,
                      seed=SEED,
                      iteration_list=2 ** np.arange(10),
                      max_attempts=500,
                      keep_percent_list=[0.25, 0.5, 0.75])
                      
    # the two data frames will contain the results
    df_run_stats, df_run_curves = mmc.run()
"""


@short_name('mimic')
class MIMICRunner(_RunnerBase):

    def __init__(self, problem, experiment_name, seed, iteration_list, population_sizes,
                 keep_percent_list, max_attempts=500, generate_curves=True, **kwargs):
        super().__init__(problem=problem, experiment_name=experiment_name, seed=seed, iteration_list=iteration_list,
                         max_attempts=max_attempts, generate_curves=generate_curves,
                         **kwargs)
        self.keep_percent_list = keep_percent_list
        self.population_sizes = population_sizes

    def run(self):
        return super().run_experiment_(algorithm=mlrose.mimic,
                                       pop_size=('Population Size', self.population_sizes),
                                       keep_pct=('Keep Percent', self.keep_percent_list))
