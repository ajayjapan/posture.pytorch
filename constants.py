"""While in development instead of args using a constants file"""

num_epochs = 2000
train_batch_size = 76
val_batch_size = 12
learning_rate = 0.001
num_workers = 10
scale = .4
default_width = 670
default_height = 760
save_interval = 20
print_freq = 10


def normalization_values():
    return 216.91674805, 51.54261398, 147.78466797, 57.77311325
