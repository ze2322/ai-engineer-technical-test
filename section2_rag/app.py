from section2_rag.rag_chain import RAGPipeline


def main():

    rag = RAGPipeline()

    print("=" * 50)
    print("Electro Pi - RAG Assistant")
    print("=" * 50)

    while True:

        question = input("\nQuestion: ")

        if question.lower() in ["exit", "quit"]:

            break

        result = rag.ask(question)

        if isinstance(result, str):

            print(result)

            continue

        print("\nAnswer:\n")

        print(result["answer"])

        print("\nSources:")

        for source in result["sources"]:

            print("-", source)


if __name__ == "__main__":

    main()