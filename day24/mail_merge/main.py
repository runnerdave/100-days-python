#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_PATH = "./Output/ReadyToSend"

def load_template() -> str:
    with open(TEMPLATE_PATH) as t:
        return t.read()
    
def list_names() -> []:
    with open(NAMES_PATH) as n:        
        lines = n.readlines()
        return [line.strip() for line in lines]

def output_letter(output, name):
    with open(OUTPUT_PATH + f"/{name}.txt", "w") as path:
        path.write(output)

if __name__ == '__main__':
    t = load_template()
    names = list_names()
    for n in names:
        o = t.replace("[name]", n)
        output_letter(o, n)
