import tensorflow as tf
import numpy as np

# Texto de entrenamiento
training_text = """
El cielo es azul,
Las nubes son blancas,
El sol brilla intensamente.
"""

# Preprocesamiento del texto
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts([training_text])
encoded_text = tokenizer.texts_to_sequences([training_text])[0]

# Crear secuencias de entrada y objetivo
max_sequence_length = 5
sequences = []
for i in range(max_sequence_length, len(encoded_text)):
    sequence = encoded_text[i-max_sequence_length:i+1]
    sequences.append(sequence)

# Dividir en entrada y objetivo
sequences = np.array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]

# Definir el modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=10, input_length=max_sequence_length),
    tf.keras.layers.LSTM(100, return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.LSTM(100),
    tf.keras.layers.Dense(len(tokenizer.word_index)+1, activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=100, verbose=0)

# Generar texto
seed_text = "El cielo"
next_words = 5

for _ in range(next_words):
    encoded_seed = tokenizer.texts_to_sequences([seed_text])[0]
    encoded_seed = tf.keras.preprocessing.sequence.pad_sequences([encoded_seed], maxlen=max_sequence_length, padding='pre')
    predicted_word_index = np.argmax(model.predict(encoded_seed))
    predicted_word = ''
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            predicted_word = word
            break
    seed_text += ' ' + predicted_word

print(seed_text)
