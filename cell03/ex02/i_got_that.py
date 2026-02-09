def main():
    prompt = "What you gotta say? : "

    while True:
        try:
            user_input = input(prompt)
        except (EOFError, KeyboardInterrupt):
            break

        if user_input == "STOP":
            break
        
        prompt = "I got that! Anything else? : "

if __name__ == "__main__":
    main()