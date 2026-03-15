import subprocess

def query_ollama(prompt):

    result = subprocess.run(
        ["ollama", "run", "llama3.2:1b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout
