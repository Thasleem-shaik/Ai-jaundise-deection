import tensorflow as tf

from preprocessing import load_datasets


# Load dataset

train_dataset, validation_dataset, test_dataset = load_datasets()


# Load trained model

model = tf.keras.models.load_model(
    "../model/jaundice_model.h5"
)


# Evaluate

results = model.evaluate(
    test_dataset,
    verbose=1
)


print("\nModel Evaluation")
print("----------------------")

for name, value in zip(model.metrics_names, results):
    print(f"{name}: {value:.4f}")