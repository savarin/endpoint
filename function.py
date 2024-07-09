def call_api(api_key):
    print(f"Calling API with {api_key}!")
    global_values = {k: v for k, v in globals().items()}

    return api_key, global_values
