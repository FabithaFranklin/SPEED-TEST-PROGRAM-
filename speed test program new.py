import time

def typing_speed_test():
    sentence = "The quick brown fox jumps over the lazy dog."
    print("Type this sentence as fast as you can:")
    print(f"\n{sentence}\n")
    
    input("Press Enter when you're ready...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words_per_minute = len(sentence.split()) / (time_taken / 60)

    if user_input == sentence:
        print(f"\n🎉 Well done! Your typing speed is {words_per_minute:.2f} WPM.")
    else:
        print("\n❌ Incorrect typing. Try again!")

typing_speed_test()