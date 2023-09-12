import streamlit as st

# Definir las preguntas y sus opciones de respuesta
preguntas = [
    {
        "pregunta": "¿Qué color es típico de las manzanas maduras?",
        "opciones": ["Verde", "Amarillo", "Rojo", "Naranja"],
        "respuesta_correcta": "Rojo"
    },
    {
        "pregunta": "¿Cuál de las siguientes frutas es la más grande?",
        "opciones": ["Fresa", "Uva", "Sandía", "Kiwi"],
        "respuesta_correcta": "Sandía"
    },
    {
        "pregunta": "¿Qué fruta es conocida por su sabor ácido?",
        "opciones": ["Banana", "Naranja", "Limón", "Pera"],
        "respuesta_correcta": "Limón"
    },
    {
        "pregunta": "¿De dónde es originaria la piña?",
        "opciones": ["Brasil", "Hawaii", "Australia", "Italia"],
        "respuesta_correcta": "Brasil"
    },
    {
        "pregunta": "¿Cuál de estas frutas contiene vitamina C en grandes cantidades?",
        "opciones": ["Plátano", "Kiwi", "Mango", "Uva"],
        "respuesta_correcta": "Kiwi"
    },
    {
        "pregunta": "¿Cuál es la fruta principal en una ensalada Waldorf?",
        "opciones": ["Manzana", "Naranja", "Pera", "Fresa"],
        "respuesta_correcta": "Manzana"
    },
    {
        "pregunta": "¿Qué fruta es conocida por su alto contenido de potasio?",
        "opciones": ["Sandía", "Pera", "Banana", "Kiwi"],
        "respuesta_correcta": "Banana"
    },
    {
        "pregunta": "¿Cuál de estas frutas es una baya?",
        "opciones": ["Plátano", "Fresa", "Mango", "Naranja"],
        "respuesta_correcta": "Fresa"
    },
    {
        "pregunta": "¿Cuál de las siguientes frutas es originaria de América?",
        "opciones": ["Mango", "Manzana", "Naranja", "Maíz"],
        "respuesta_correcta": "Maíz"
    },
    {
        "pregunta": "¿Cuál es la fruta más consumida en el mundo?",
        "opciones": ["Naranja", "Banana", "Manzana", "Uva"],
        "respuesta_correcta": "Banana"
    },
    {
        "pregunta": "¿Qué fruta se asocia comúnmente con el Día de San Valentín?",
        "opciones": ["Manzana", "Uva", "Fresa", "Kiwi"],
        "respuesta_correcta": "Fresa"
    },
    {
        "pregunta": "¿Cuál de estas frutas es rica en fibra?",
        "opciones": ["Naranja", "Sandía", "Pera", "Kiwi"],
        "respuesta_correcta": "Pera"
    },
    {
        "pregunta": "¿Qué fruta se utiliza para hacer jugo de naranja?",
        "opciones": ["Naranja", "Mango", "Fresa", "Pera"],
        "respuesta_correcta": "Naranja"
    },
    {
        "pregunta": "¿Qué fruta es conocida por ser un símbolo de la paz?",
        "opciones": ["Banana", "Kiwi", "Pera", "Manzana"],
        "respuesta_correcta": "Manzana"
    },
    {
        "pregunta": "¿Cuál de estas frutas es conocida por ser un afrodisíaco?",
        "opciones": ["Fresa", "Sandía", "Uva", "Mango"],
        "respuesta_correcta": "Sandía"
    }
]

# Inicializar el contador de respuestas correctas
puntaje = 0

# Título de la aplicación
st.title("Trivia de Frutas")

# Mostrar las preguntas y opciones de respuesta
for i, pregunta_data in enumerate(preguntas):
    pregunta = pregunta_data["pregunta"]
    opciones = pregunta_data["opciones"]
    respuesta_correcta = pregunta_data["respuesta_correcta"]

    # Mostrar la pregunta
    st.write(f"**Pregunta {i+1}:** {pregunta}")

    # Mostrar las opciones de respuesta
    opcion_seleccionada = st.radio("Elige una respuesta:", opciones)

    # Verificar si la respuesta es correcta
    if opcion_seleccionada == respuesta_correcta:
        st.write("¡Correcto!")
        puntaje += 1
    else:
        st.write(f"Respuesta incorrecta. La respuesta correcta es: {respuesta_correcta}")

# Mostrar el puntaje final y un mensaje de motivación
st.subheader("Resultados:")
st.write(f"Puntaje Total: {puntaje} / {len(preguntas)}")

if puntaje >= len(preguntas) * 0.7:
    st.write("¡Excelente! ¡Eres un experto en frutas! 🍏🍌🍓")
else:
    st.write("Sigue aprendiendo sobre las frutas y sus beneficios para la salud. 🍎🍊🍇")
