response={
    "hello":"Hi there!,How can i help you",
    "hi":"hey! Good to see you",
    "how are you":"I am doing good, how about you?",
    "what is your name":"I am a Rule based chatbot",
    "assistance":"Sure! I am here to assist you. What do you need assistance with?",
    "help":"You can talk to me using greetings or type bye to exit",
    "who created you":"I was created by Monika dey",
    "thank you":"you are welcome"
}
while True:
    raw_input=input("You:")
    clean_input=raw_input.lower().strip()

    if clean_input == "bye":
        print("Bot: Goodbye!")
        break

    reply=response.get(clean_input,"Sorry I didn't understand can you reprase that?")
    print("Bot:",reply)
