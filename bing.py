from bardapi import Bard
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
def is_a_question(input):
    prompt="I am going to provide a phrase and i just need you to answer whether it  is a statement or a question. Answer with 'statement'  if its a statement and with  'question' if its a question. phrase : "
    prompt+=input
    response = str(call_bard(prompt))
    if response.find("question")!=-1 or response.find("Question")!=-1:
        return True
    else :
        return False

def related_to_climat_change(input):
    prompt = "I am going to provide information that might be right or wrong that doesnt metter i just need you to answer whether it relates to climate change or doesnt  . Answer with yes if it relates to climate change even if its incorrect or a false statement and answer with  no if it doesnt relate at all. information: "
    prompt+=input
    response = str(call_bard(prompt))
    if response[0:10].find("yes") != -1 or response[0:10].find("Yes") != -1 or response[0:10].find("oui") != -1 or response[0:10].find("Oui") != -1:
        return True
    else :
        return False
def get_answer_to_question(input):
    response = str(call_bard(input+" ,answer in less than 200 words "))
    return response
def get_answer_for_statement(input):
    prompt = "im going to provide a statement in regards of climate change , your task is to say wether that statement is right or wrong then provide information about it with links to resources . start by saying 'you are correct' if the statement if correct or start by saying 'that statement is uncorrect' if the statement is uncorrect, statement: "
    prompt += input
    response = str(call_bard(prompt))
    return response
load_dotenv()
_BARD_API_KEY="dAhXema_ITmLrz3VNN4E5ohkxmFWiA0qddbCkXTR60jtZCpp2VQCcyJLS5c-mbY76BbHqw."


def call_bard(query):
    bard = Bard(_BARD_API_KEY)
    answer = bard.get_answer(query)
    return (answer['content'])
def proccess_input(inp):
    answer=""
    if related_to_climat_change(inp):
        if is_a_question(inp):
            answer = get_answer_to_question(inp)
        else:
            answer=get_answer_for_statement(inp)
    else:
        answer="Kindly provide a statement pertaining to climate change or pose a question related to this critical global issue."

    translated = GoogleTranslator(source='auto', target='fr').translate(answer)
    return translated

#print(proccess_input("le changement climatique est dangereux"))