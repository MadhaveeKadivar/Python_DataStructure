def create_set():
    num_of_values = int(input("\nEnter how many values you want to add in set : "))
    new_set = {input(f"\nEnter {i}th value : ") for i in range(num_of_values) }
    return new_set