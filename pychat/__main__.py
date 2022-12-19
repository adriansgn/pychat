import openai
import os
import argparse

OPENAI_API_KEY = 'OPENAI_API_KEY'

def main():
    openai_api_key = os.getenv(OPENAI_API_KEY)

    parser = argparse.ArgumentParser(description="Pychat v0.1")
    parser.add_argument("--max-tokens", help="Maximum size of tokens to be used", type=int, default=4000)
    parser.add_argument("--engine", help="The openai engine to use", type=str, default='text-davinci-003')
    parser.add_argument("--query", help="checkinng for user input", type=str,required=True)


    args = parser.parse_args()
    max_tokens = args.max_tokens #flag galing sa parser.add_argument
    engine = args.engine
    query = args.query

    if openai_api_key == None:
        print('OPENAI_API_KEY required')
        exit(-1)

    while query != 'quit':
        test_input = query.strip()

        if test_input:
            completion = openai.Completion.create(
                engine=engine, prompt=query, max_tokens=max_tokens
            )
            if len(completion.choices) == 0:
                print("No output")

            else:
                output = completion.choices[0].text
                print("Output: {}".format(output))

            query = input("Input (quit to exit): ").strip()

        else:
            print('Invalid input')

    print("\nPowered by openai")




if __name__ == '__main__':
    main()