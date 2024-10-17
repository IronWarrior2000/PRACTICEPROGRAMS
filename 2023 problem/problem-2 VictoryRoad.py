def victory_road():
    num_steps = int(input('num steps: '))
    danger_steps = int(input('dangerous steps count: '))
    dangerous_steps_to_avoid = input('Type steps to avoid: ')

    dangerous_steps = list(dangerous_steps.split())

    count = 0

    for i in range(0, num_steps):
        step_path.append(i)

    for i in range(0, num_steps):
        if step_path[i] or step_path[i+1] == dangerous_steps:
            count-=1
        else:
            count+=1
    print(count)

m ,   

def main():
    victory_road()

main()