'''Invest one dollar and sit'''


import random
import itertools

def ben_return_given_trajectory(traj):
    '''Ben'''
    X = 1
    Y = 0
    data = []
    for z_i in traj:
        # If HEADS money doubles
        if z_i == 0:
            Y += 2*X
        # If TAILS money halves
        else:
            Y -= 0.5*X

        data.append(Y)

    return data, Y

def steve_return_given_trajectory(traj):
    '''Steves strategy'''
    
    X = 1
    Y = X
    data = []
    for z_i in traj:
        # If HEADS money doubles
        if z_i == 0:
            Y = 2*Y
        # If TAILS money halves
        else:
            Y = Y/2

        data.append(Y)

    return data, Y

def tom_return_given_trajectory(traj):
    '''Toms strategy'''
    
    X = 1
    cash = X/2
    stock = X/2
    curr_stock = 0 
    data = []
    for z_i in traj:
        # If HEADS money doubles
        if z_i == 0:
            curr_stock = 2*stock
        # If TAILS money halves
        else:
            curr_stock = 0.5*stock

        # Re-balance
        Y = curr_stock + cash
        cash = Y/2
        stock = Y/2

        data.append(Y)

    return data, Y

if __name__ == '__main__':

    TIME = 10
    plot = {'steve': [], 'ben': []}
    
    trajectories = list(itertools.product([0, 1], repeat=10))
    random.shuffle(trajectories)
    for idx, traj in enumerate(trajectories):
        rewards, _ = steve_return_given_trajectory(traj)
        plot['steve'].append(rewards)

        rewards, _ = ben_return_given_trajectory(traj)
        plot['ben'].append(rewards)
        
        if idx == 5:
            break

        print(rewards)
