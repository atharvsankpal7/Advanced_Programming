while True:
    try:
        task = input("Enter a task (or 'q' to quit): ")
        if task == 'q':
            break
        print(task+" is done.")
    except Exception as e:
        print("An error occurred:", e)
