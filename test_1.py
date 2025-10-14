from langchain_service import PromptOllamaSbS
from langchain_service import BasicQuery


def main():
    print("Starting Ollama SbS test")
    query = BasicQuery(question="cuanto mide una ballena azul?")
    PromptOllamaSbS(query)

if __name__ == "__main__":
    main()