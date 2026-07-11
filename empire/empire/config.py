AVAILABLE_MODELS = [
    "qwen2.5-coder:7b",
    "deepseek-r1:7b",
    "gemma3:4b",
]

MODEL_NAME = AVAILABLE_MODELS[0]


def get_current_model():
    return MODEL_NAME


def set_current_model(model_name):
    global MODEL_NAME
    MODEL_NAME = model_name
