import openai
import os

OPENAI_API_KEY='OPENAI_API_KEY'

def main():
    openai_api_key = os.getenv(OPENAI_API_KEY)

    if openai_api_key == None:
        print('OPENAI_API_KEY required')
        exit(-1)

    print("Pychat v0.1")
    query = input('Input: ')
    completion = openai.Completion.create(engine='text-davinci-003', prompt=query, max_tokens=4000)
    output = completion.choices[0].text
    print("Output: {}".format(output))

if __name__ == '__main__':
    main()