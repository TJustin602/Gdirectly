import random 
#use this library: The random.random() function generates random floating numbers in the range of 0.1, and 1.0. 

def assign_recipients(target_distribution, recipients):
    # confirm that the weights in target_distribution sum to 1.0
    if not (1.0 - 1e-10 <= sum(target_distribution.values()) <= 1.0 + 1e-10):
        raise ValueError("Target distribution weights need to have sum of 1.0")

    # Create a list of tuples with payment configurations and weights: So i like to take opportunities and try libraries / functions that are 'pre built' and I thought this one would be a great learning opportunity for me, so I went with it: https://www.askpython.com/python/list/python-list-of-tuples
    payment_configs = list(target_distribution.items())

    # Initialize an empty dictionary to store the assigned payment configurations for the recipients
    assigned_configs = {}

    # go through each recipient and assign a payment configuration
    for recipient in recipients:
        # and then randomly choose a payment based on the specified weights
        chosen_config = random.choices(payment_configs, weights=[weight for config, weight in payment_configs])[0][0]

        # Allocate a payment configuration to the recipient
        assigned_configs[recipient] = chosen_config

    return assigned_configs

# lets set up our 'payload'
target_distribution = {"A": 0.3, "B": 0.2, "C": 0.5}
recipients = ["Diogo", "Piali", "Solomon", "Gisele", "Jeff", "Falida", "Ade", "Maya", "Meylakh", "Nana"]
outputs = assign_recipients(target_distribution, recipients)

# output: The payment distribs for each recipient
print(outputs)
