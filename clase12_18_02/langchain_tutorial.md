# Tutorial Básico de LangChain

## ¿Qué es LangChain?

LangChain es un framework que facilita la creación de aplicaciones usando modelos de lenguaje (LLMs). Permite desarrollar aplicaciones más complejas y potentes combinando diferentes capacidades de los LLMs con otras herramientas y fuentes de datos.

## Instalación

```bash
pip install langchain openai python-dotenv
```

## Configuración Inicial

```python
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo
llm = OpenAI(temperature=0.7)
```

## Conceptos Básicos

### 1. Prompts y Templates

Los templates permiten crear prompts dinámicos con variables:

```python
# Definir un template
prompt_template = PromptTemplate(
    input_variables=["producto"],
    template="Genera 3 nombres creativos para un {producto}."
)

# Usar el template
prompt = prompt_template.format(producto="robot aspiradora")
```

### 2. Chains (Cadenas)

Las chains permiten combinar diferentes componentes en un flujo:

```python
# Crear una chain simple
chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Ejecutar la chain
resultado = chain.run("robot aspiradora")
print(resultado)
```

### 3. Memory (Memoria)

La memoria permite mantener un contexto en conversaciones:

```python
# Crear memoria para conversación
memory = ConversationBufferMemory()

# Crear template con memoria
template = """
Conversación actual:
{chat_history}
Humano: {input}
AI:"""

prompt_template = PromptTemplate(
    input_variables=["chat_history", "input"],
    template=template
)

# Crear chain con memoria
chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    memory=memory,
    verbose=True
)

# Ejemplo de uso
respuesta1 = chain.run("¿Cuál es la capital de Francia?")
respuesta2 = chain.run("¿Qué otros datos interesantes conoces sobre esta ciudad?")
```

## Ejemplo Práctico: Asistente de Viajes

```python
from langchain.chains import SimpleSequentialChain

# Chain para generar destino
template_destino = PromptTemplate(
    input_variables=["presupuesto"],
    template="Sugiere un destino turístico para un presupuesto de {presupuesto} dólares."
)
chain_destino = LLMChain(llm=llm, prompt=template_destino)

# Chain para generar actividades
template_actividades = PromptTemplate(
    input_variables=["destino"],
    template="Sugiere 3 actividades principales para hacer en {destino}."
)
chain_actividades = LLMChain(llm=llm, prompt=template_actividades)

# Combinar chains
chain_completa = SimpleSequentialChain(
    chains=[chain_destino, chain_actividades],
    verbose=True
)

# Ejecutar cadena completa
resultado = chain_completa.run("1000")
```

## Mejores Prácticas

1. **Variables de Entorno**: Siempre usa variables de entorno para las API keys:
```python
# .env
OPENAI_API_KEY=tu-api-key
```

2. **Control de Temperatura**: Ajusta la temperatura según necesites respuestas más creativas (alta) o más precisas (baja):
```python
llm = OpenAI(temperature=0.3)  # Más preciso
llm = OpenAI(temperature=0.8)  # Más creativo
```

3. **Manejo de Errores**: Implementa manejo de errores para las llamadas a la API:
```python
try:
    resultado = chain.run(input)
except Exception as e:
    print(f"Error: {e}")
```

## Recursos Adicionales

- [Documentación Oficial de LangChain](https://python.langchain.com/docs/get_started/introduction.html)
- [Ejemplos de LangChain en GitHub](https://github.com/hwchase17/langchain)
- [Guía de Prompts](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)

## Notas Importantes

- Asegúrate de tener suficientes créditos en tu cuenta de OpenAI
- Monitorea el uso de tokens para controlar costos
- Considera las limitaciones de rate limit de la API
- Guarda los resultados importantes para evitar llamadas API innecesarias
