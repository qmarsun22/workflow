import openai
import os
import traceback
from retrying import retry
import pprint
import json
#http://proxy.example.com/proxy.pac

#curl https://api.openai.com/v1/models -H "Authorization: Bearer sk-

#https://community.openai.com/t/how-can-i-disable-ssl-verification-when-using-openai-api-in-python/110837

@retry(stop_max_attempt_number=5)
def make_create():
    try:
        print("call openai")
        import json

        # Opening JSON file
        mykeys = json.load(open('C:\workarea\open-ai-api-keys.json'))
        pprint.pprint(mykeys)
        client = OpenAI(api_key=mykeys.api_key,
                 organization=mykeys.organization)

        response = client.embeddings.create(input="test", 
                                             model="gpt-3.5-turbo-0613")
        print(response)
    except Exception as e:
        pass

    
def test3():
    print("debug calling test3")
    from openai import OpenAI
    mykeys = json.load(open('C:\workarea\open-ai-api-keys.json'))
    pprint.pprint(mykeys)
    #client = OpenAI(api_key=mykeys.api_key,organization=mykeys.organization)
    
    client = OpenAI(api_key=mykeys["api_key"],
                 organization=mykeys["organization"])
    print(client)
    openai.verify_ssl_certs = False
    
    
    print("before calling client.chat.completions.create")
    try:
        completion = client.chat.completions.create(
            #model="gpt-3.5-turbo",
            model="text-embedding-3-small",
            messages=[
            #   {"role" : "user", "content" :"what is name expensive whiskey and price give short answer"}
            # {"role" : "user", "content" : "what features removed from apachetomcat 9.05 compare to apachetomcat 8.5.31"
            {'role':"user","content":" what standardcontext.getservlets"
                }
            ])
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        print(dir(e))
        print(e.code)
        print(e.body)
        print(e.request)
        print(e.args)
    except openai.RateLimitError as e:
       print("A 429 status code was received; we should back off a bit.")
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)
        print("done completion")
        print(completion)
        print(completion.choices)




def old_test4():
    openai.api_key = "sk-

    response = openai.Completion.create(
        engine="gpt-4",
        #model = 'gpt-4',
        prompt = 'TEST',
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

try:
   #make_create()
   #test2()
   test3()
  #Make your OpenAI API request here
   # response = client.chat.completions.create(
    #model="gpt-3.5-turbo",
   # messages=[
   #     {"role": "system", "content": "You are a helpful assistant."},
   #     {"role": "user", "content": "Who won the world series in 2020?"},
   #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
   #     {"role": "user", "content": "Where was it played?"}
   # ],

    #chat_test_response  = client.chat.completions.create(
    #        model="gpt-3.5-turbo-0613",
    #        messages=[ { "role": "user","content":"tell me story" }],
      #  temperature=0,)    
    #print(chat_test_response)                            
except Exception as e:
  #Handle rate limit error (we recommend using exponential backoff)
  print(f"OpenAI API request exceeded rate limit: {e}")
  pass