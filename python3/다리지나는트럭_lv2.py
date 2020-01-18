def solution(bridge_length, weight, truck_weights):
    total_len = len(truck_weights)
    bridge = []
    finish = []
    time = 0
    sum = 0
    
    while len(finish) != total_len:
        time += 1
        if len(bridge) == bridge_length:
            temp = bridge.pop(0)
            if temp > 0:
                finish.append(temp)
                sum -= temp
        if len(bridge) < bridge_length:
            if truck_weights and (sum + truck_weights[0]) <= weight:
                sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) 

    return time
