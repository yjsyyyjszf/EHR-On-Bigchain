from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.utils import EndpointConfig
from rasa_core.training import interactive
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy

logger = logging.getLogger(__name__)

def train_agent(interpreter,
                domain_file="domain.yml",
                training_file='data/stories.md'):

    fallback = FallbackPolicy(fallback_action_name='action_default_fallback',
                              core_threshold = 0.3,
                              nlu_threshold=0.1)

    action_endpoint = EndpointConfig('http://localhost:5055/webhook')
    policies = [MemoizationPolicy(max_history=6),
                KerasPolicy(max_history=6, epochs=100, batch_size=4),
                fallback]
    agent = Agent(domain_file, policies=policies,
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)
    stories = agent.load_data(training_file)
    agent.train(stories)
    interactive.run_interactive_learning(agent)

    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    interpreter = RasaNLUInterpreter('./models/current/nlu')
    train_agent(interpreter)
