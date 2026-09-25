import os
import tensorflow as tf

from preprocessing import load_datasets


IMG_SIZE = (224, 224)


# ---------------- LOAD DATA ----------------

train_dataset, validation_dataset, test_dataset = load_datasets()


# ---------------- DATA AUGMENTATION ----------------

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.05),
    tf.keras.layers.RandomZoom(0.1),
])


# ---------------- BASE MODEL ----------------

base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False


# ---------------- MODEL ----------------

inputs = tf.keras.Input(shape=(224, 224, 3))

x = data_augmentation(inputs)

x = tf.keras.layers.Rescaling(
    1.0 / 127.5,
    offset=-1
)(x)

x = base_model(x, training=False)

x = tf.keras.layers.GlobalAveragePooling2D()(x)

x = tf.keras.layers.Dropout(0.3)(x)

outputs = tf.keras.layers.Dense(
    1,
    activation="sigmoid"
)(x)

model = tf.keras.Model(inputs, outputs)


# ---------------- COMPILE ----------------

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0001
    ),
    loss="binary_crossentropy",
    metrics=[
        "accuracy",
        tf.keras.metrics.Precision(name="precision"),
        tf.keras.metrics.Recall(name="recall")
    ]
)


# ---------------- TRAIN ----------------

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)


# ---------------- SAVE MODEL ----------------

os.makedirs("../model", exist_ok=True)

model.save("../model/jaundice_model.h5")

print("Model saved successfully!")