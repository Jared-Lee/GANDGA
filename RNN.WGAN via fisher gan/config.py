import os
import time

import tensorflow as tf
from tensorflow.contrib.rnn import GRUCell
from highway_rnn_cell import RHNCell

tf.logging.set_verbosity(tf.logging.INFO)

flags = tf.app.flags




flags.DEFINE_string('LOGS_DIR', './logs/', '')
flags.DEFINE_string('DATA_DIR', '../Dataset/AlexaTop1M_NoSeparate', "")
flags.DEFINE_string('CKPT_PATH', "./ckpt/", "")
flags.DEFINE_integer('BATCH_SIZE', 64, '')
flags.DEFINE_integer('CRITIC_ITERS', 5, """When training wgan, it is helpful to use 
    10 critic_iters, however, when training with fgan, 2 critic iters may be more suitable.""")
flags.DEFINE_integer('LAMBDA', 10, '')
flags.DEFINE_integer('MAX_N_EXAMPLES', 10000000, '')
flags.DEFINE_string('GENERATOR_MODEL', 'Generator_RNN_CL_VL_TH', '')
flags.DEFINE_string('DISCRIMINATOR_MODEL', 'Discriminator_RNN', '')
flags.DEFINE_string('PICKLE_PATH', './pkl', '')
flags.DEFINE_integer('GEN_ITERS', 20, """When training wgan, it is helpful to use 
    50 gen_iters, however, when training with fgan, 2 gen_iters may be more suitable.""")
#flags.DEFINE_integer('ITERATIONS_PER_SEQ_LENGTH', 15000, '')
flags.DEFINE_integer('ITERATIONS_PER_SEQ_LENGTH', 15000, '')
flags.DEFINE_float('NOISE_STDEV', 10.0, '')

flags.DEFINE_boolean('TRAIN_FROM_CKPT', False, '')

# RNN Settings
flags.DEFINE_integer('GEN_RNN_LAYERS', 1, '')
flags.DEFINE_integer('DISC_RNN_LAYERS', 1, '')
flags.DEFINE_integer('DISC_STATE_SIZE', 512, '')
flags.DEFINE_integer('GEN_STATE_SIZE', 512, '')
flags.DEFINE_string('RNN_CELL', 'gru', """Choose between 'gru' or 'rhn'.
    'gru' option refers to a vanilla gru implementation
    'rhn' options refers to a multiplicative integration 2-layer highway rnn
        with normalizing tanh activation
    """)

flags.DEFINE_integer('START_SEQ', 32, '')
flags.DEFINE_integer('END_SEQ', 33, '')
flags.DEFINE_bool('PADDING_IS_SUFFIX', False, '')
flags.DEFINE_integer('SAVE_CHECKPOINTS_EVERY', 3000, '')
flags.DEFINE_boolean('LIMIT_BATCH', True, '')
flags.DEFINE_boolean('SCHEDULE_ITERATIONS', False, '')
flags.DEFINE_integer('SCHEDULE_MULT', 2000, '')
flags.DEFINE_boolean('DYNAMIC_BATCH', False, '')
flags.DEFINE_string('SCHEDULE_SPEC', 'all', '')

# Print Options
flags.DEFINE_boolean('PRINT_EVERY_STEP', False, '')
flags.DEFINE_integer('PRINT_ITERATION', 1000, '')


# Fisher GAN Flags
flags.DEFINE_string('GAN_TYPE', 'fgan', "Type of GAN to use. Choose between 'wgan' and 'fgan' for wasserstein and fisher respectively")
flags.DEFINE_float('FISHER_GAN_RHO', 1e-6, "Weight on the penalty term for (sigmas -1)**2")

# Learning Rates
flags.DEFINE_float('DISC_LR', 2e-4, """Disc learning rate -- should be different than generator
    learning rate due to TTUR paper https://arxiv.org/abs/1706.08500""")
flags.DEFINE_float('GEN_LR', 1e-4, """Gen learning rate""")



# Only for inference mode

flags.DEFINE_string('INPUT_SAMPLE', './output/sample.txt', '')


FLAGS = flags.FLAGS

# only for backward compatability

LOGS_DIR = os.path.join(FLAGS.LOGS_DIR,
                        "%s-%s-%s-%s-%s-%s-%s-" % (FLAGS.GENERATOR_MODEL, FLAGS.DISCRIMINATOR_MODEL,
                                                        FLAGS.GEN_ITERS, FLAGS.CRITIC_ITERS,
                                                        FLAGS.DISC_STATE_SIZE, FLAGS.GEN_STATE_SIZE,
                                                        time.time()))


class RestoreConfig():
    def __init__(self):
        if FLAGS.TRAIN_FROM_CKPT:
            self.restore_dir = self.set_restore_dir(load_from_curr_session=False)
        else:
            self.restore_dir = self.set_restore_dir(load_from_curr_session=True)

    def set_restore_dir(self, load_from_curr_session=True):
        if load_from_curr_session:
            restore_dir = os.path.join(LOGS_DIR, 'checkpoint')
        else:
            restore_dir = FLAGS.CKPT_PATH
        return restore_dir

    def get_restore_dir(self):
        return self.restore_dir


def create_logs_dir():
    os.makedirs(LOGS_DIR)

restore_config = RestoreConfig()
DATA_DIR = FLAGS.DATA_DIR
BATCH_SIZE = FLAGS.BATCH_SIZE
CRITIC_ITERS = FLAGS.CRITIC_ITERS
LAMBDA = FLAGS.LAMBDA
MAX_N_EXAMPLES = FLAGS.MAX_N_EXAMPLES
PICKLE_PATH = FLAGS.PICKLE_PATH
PICKLE_LOAD = True
CKPT_PATH = FLAGS.CKPT_PATH
GENERATOR_MODEL = FLAGS.GENERATOR_MODEL
DISCRIMINATOR_MODEL = FLAGS.DISCRIMINATOR_MODEL
GEN_ITERS = FLAGS.GEN_ITERS

if FLAGS.RNN_CELL.lower() == 'gru':
    RNN_CELL = GRUCell
elif FLAGS.RNN_CELL.lower() == 'rhn':
    RNN_CELL = RHNCell
else:
    raise ValueError('improper rnn cell type selected')