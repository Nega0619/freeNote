from string import ascii_uppercase
import numpy as np
import pandas as pd
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

#Hyperparameters
learning_rate = 0.0002
gamma         = 0.98 # 무조건 끝나는 episode라면 gamma == 1도 가능하다.

# reward
move_reward = 0.1
obs_reward = 0.1
goal_reward = 10
back_reward = -0.1
print('reward:' , move_reward, obs_reward, goal_reward, back_reward)

# etc
max_cum_reward = -9999999999999999

# 저장할 파일 이름
my_file_name='REINFORCE_4_noback_gdbd_'+str(move_reward)+'_'+str(obs_reward)+'_'+str(goal_reward)

local_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

class Simulator:
    def __init__(self):
        '''
        height : 그리드 높이
        width : 그리드 너비
        inds : A ~ Q alphabet list
        '''
        # Load train data
        self.files = pd.read_csv(os.path.join(local_path, "./data/factory_order_train.csv"))
        self.height = 10
        self.width = 9
        self.inds = list(ascii_uppercase)[:17]

    def set_box(self):
        '''
        아이템들이 있을 위치를 미리 정해놓고 그 위치 좌표들에 아이템이 들어올 수 있으므로 그리드에 100으로 표시한다.
        데이터 파일에서 이번 에피소드 아이템 정보를 받아 가져와야 할 아이템이 있는 좌표만 -100으로 표시한다.
        self.local_target에 에이전트가 이번에 방문해야할 좌표들을 저장한다.
        따라서 가져와야하는 아이템 좌표와 end point 좌표(처음 시작했던 좌표로 돌아와야하므로)가 들어가게 된다.
        '''
        box_data = pd.read_csv(os.path.join(local_path, "./data/box.csv"))

        # 물건이 들어있을 수 있는 경우
        for box in box_data.itertuples(index = True, name ='Pandas'):
            self.grid[getattr(box, "row")][getattr(box, "col")] = 100

        # 물건이 실제 들어있는 경우
        order_item = list(set(self.inds) & set(self.items))
        order_csv = box_data[box_data['item'].isin(order_item)]

        for order_box in order_csv.itertuples(index = True, name ='Pandas'):
            self.grid[getattr(order_box, "row")][getattr(order_box, "col")] = -100
            # local target에 가야 할 위치 좌표 넣기
            self.local_target.append(
                [getattr(order_box, "row"),
                 getattr(order_box, "col")]
            )

        self.local_target.append([9,4])

        # 알파벳을 Grid에 넣어서 -> grid에 2Dconv 적용 가능

    def set_obstacle(self):
        '''
        장애물이 있어야하는 위치는 미리 obstacles.csv에 정의되어 있다. 이 좌표들을 0으로 표시한다.
        '''
        obstacles_data = pd.read_csv(os.path.join(local_path, "./data/obstacles.csv"))
        for obstacle in obstacles_data.itertuples(index = True, name ='Pandas'):
            self.grid[getattr(obstacle, "row")][getattr(obstacle, "col")] = 0

    def reset(self, epi):
        '''
        reset()은 첫 스텝에서 사용되며 그리드에서 에이전트 위치가 start point에 있게 한다.
        :param epi: episode, 에피소드 마다 가져와야 할 아이템 리스트를 불러올 때 사용
        :return: 초기셋팅 된 그리드
        :rtype: numpy.ndarray
        _____________________________________________________________________________________
        items : 이번 에피소드에서 가져와야하는 아이템들
        terminal_location : 현재 에이전트가 찾아가야하는 목적지
        local_target : 한 에피소드에서 찾아가야하는 아이템 좌표, 마지막 엔드 포인트 등의 위치좌표들
        actions: visualization을 위해 에이전트 action을 저장하는 리스트
        curloc : 현재 위치
        '''

        # initial episode parameter setting
        self.epi = epi
        self.items = list(self.files.iloc[self.epi])[0]
        self.cumulative_reward = 0
        self.terminal_location = None
        self.local_target = []
        self.actions = []

        # initial grid setting
        self.grid = np.ones((self.height, self.width), dtype="float16")

        # set information about the gridworld
        self.set_box()
        self.set_obstacle()

        # start point를 grid에 표시
        self.curloc = [9, 4]
        self.grid[int(self.curloc[0])][int(self.curloc[1])] = -5

        self.done = False

        return self.grid

    def apply_action(self, action, cur_x, cur_y):
        '''
        에이전트가 행한 action대로 현 에이전트의 위치좌표를 바꾼다.
        action은 discrete하며 4가지 up,down,left,right으로 정의된다.

        :param x: 에이전트의 현재 x 좌표
        :param y: 에이전트의 현재 y 좌표
        :return: action에 따라 변한 에이전트의 x 좌표, y 좌표
        :rtype: int, int
        '''
        new_x = cur_x
        new_y = cur_y
        # up
        if action == 0:
            new_x = cur_x - 1
        # down
        elif action == 1:
            new_x = cur_x + 1
        # left
        elif action == 2:
            new_y = cur_y - 1
        # right
        else:
            new_y = cur_y + 1

        return int(new_x), int(new_y)


    def get_reward(self, new_x, new_y, out_of_boundary):
        '''
        get_reward함수는 리워드를 계산하는 함수이며, 상황에 따라 에이전트가 action을 옳게 했는지 판단하는 지표가 된다.
        :param new_x: action에 따른 에이전트 새로운 위치좌표 x
        :param new_y: action에 따른 에이전트 새로운 위치좌표 y
        :param out_of_boundary: 에이전트 위치가 그리드 밖이 되지 않도록 제한
        :return: action에 따른 리워드
        :rtype: float
        '''

        # 바깥으로 나가는 경우
        if any(out_of_boundary):
            reward = obs_reward

        else:
            # 장애물에 부딪히는 경우
            if self.grid[new_x][new_y] == 0:
                reward = obs_reward

                # 현재 목표에 도달한 경우
            elif new_x == self.terminal_location[0] and new_y == self.terminal_location[1]:
                reward = goal_reward

            # 그냥 움직이는 경우
            else:
                if len(self.actions)>1 and self.actions[-2]==(new_x,new_y):
                    reward = back_reward
                else :
                    reward = move_reward

        return reward

    def step(self, action):
        '''
        에이전트의 action에 따라 step을 진행한다.
        action에 따라 에이전트 위치를 변환하고, action에 대해 리워드를 받고, 어느 상황에 에피소드가 종료되어야 하는지 등을 판단한다.
        에이전트가 endpoint에 도착하면 gif로 에피소드에서 에이전트의 행동이 저장된다.
        :param action: 에이전트 행동
        :return:
            grid, 그리드
            reward, 리워드
            cumulative_reward, 누적 리워드
            done, 종료 여부
            goal_ob_reward, goal까지 아이템을 모두 가지고 돌아오는 finish율 계산을 위한 파라미터
        :rtype: numpy.ndarray, float, float, bool, bool/str
        (Hint : 시작 위치 (9,4)에서 up말고 다른 action은 전부 장애물이므로 action을 고정하는 것이 좋음)
        '''

        self.terminal_location = self.local_target[0]
        cur_x,cur_y = self.curloc
        self.actions.append((cur_x, cur_y))

        new_x, new_y = self.apply_action(action, cur_x, cur_y)

        out_of_boundary = [new_x < 0, new_x >= self.height, new_y < 0, new_y >= self.width]

        # 바깥으로 나가는 경우 종료
        if any(out_of_boundary):
            self.done = True
            goal_ob_reward = 'die'
        else:
            # 장애물에 부딪히는 경우 종료
            if self.grid[new_x][new_y] == 0:
                self.done = True
                goal_ob_reward = 'die'

            # 현재 목표에 도달한 경우, 다음 목표설정
            elif new_x == self.terminal_location[0] and new_y == self.terminal_location[1]:

                # end point 일 때
                if [new_x, new_y] == [9,4]:
                    self.done = True

                self.local_target.remove(self.local_target[0])
                self.grid[cur_x][cur_y] = 1
                self.grid[new_x][new_y] = -5
                goal_ob_reward = 'goal'
                self.curloc = [new_x, new_y]
            else:
                # 그냥 움직이는 경우
                self.grid[cur_x][cur_y] = 1
                self.grid[new_x][new_y] = -5
                self.curloc = [new_x,new_y]
                goal_ob_reward = 'move'

        # 보상 계산하기
        reward = self.get_reward(new_x, new_y, out_of_boundary)

        self.cumulative_reward += reward

        if self.done == True:
            if [new_x, new_y] == [9, 4]:
                if self.terminal_location == [9, 4]:
                    # 완료되면 GIFS 저장
                    goal_ob_reward = 'finish'

        return self.get_current_state(), reward, self.cumulative_reward, self.done, goal_ob_reward

    def get_current_state(self):
        state = (self.curloc[0], self.curloc[1], self.local_target[0][0], self.local_target[0][1])
        return np.array(state)

class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.data = []

        # weight를 정의
        self.fc1 = nn.Linear(4, 128) # fully connected first layer
        self.fc2 = nn.Linear(128, 4) # fully connected second layer

        # optimizer
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)

    # 얜 언제 불러지는걸까요?
    def forward(self, x):
        x = F.relu(self.fc1(x)) # first layer 통과 후 비선형 함수 통과
        x = F.softmax(self.fc2(x), dim=0) # second layer 통과 후 sofrmax로 합이 1이 되는 확률로 만들어
        return x

    # s, a pair 저장
    def put_data(self, item):
        self.data.append(item)

    # 2-(C) presudo code
    def train_net(self):
        R = 0
        self.optimizer.zero_grad()
        for r, prob in self.data[::-1]: # return을 재귀적으로 뒤에서부터 더하면서 계산
            R = r + gamma * R # Return Gt
            loss = -torch.log(prob) * R # loss function
            loss.backward() # gradient 계산
        self.optimizer.step() # Adam optimizer update 진해
        self.data = []

# MAIN

files = pd.read_csv('./data/factory_order_train.csv')
episodes = len(files)

env = Simulator()
pi = Policy()

max_cum_reward = -99999

# ########################################################
# 액션 저장하는 txt파일 만들기
f = open(my_file_name+'.txt', 'w')
# ########################################################

for epi in range(episodes):
    state = env.reset(epi)
    state = env.get_current_state()
    print('\n\n▶▶▶{}번째 에피소드 시작, env 초기화 완료.'.format(epi))

    # 아이템 리스트 확인
    items = list(files.iloc[epi])[0]
    print('가져와야 할 아이템 : ' + list(files.iloc[epi])[0] + '\n')
    items = env.local_target

    done = False
    isFinished=False
    transitions = []

    while not done:
        prob = pi(torch.from_numpy(state).float())
        m = Categorical(prob) # prob 중 높은 확률 값을 리턴
        action = m.sample()

        state_prime, reward, cumul ,done, goal_ob_reward = env.step(action.item())
        # pi.put_data((reward, prob[action]))
        # print('action', action, 'reward', reward)

        if goal_ob_reward == 'move':
            print('move')
            transitions.append( [state, reward, prob[action]] )
        elif goal_ob_reward == 'die':
            print('die')
            transitions.append( [state, reward, prob[action]] )

            print('pre die')
            for t in transitions:
                state, reward, prob[action] = t
                if reward > 0:
                    reward = -reward
                print(reward, action)
                pi.put_data((reward, prob[action]))
            print('end die')
        elif goal_ob_reward =='goal':
            print('goal')
            transitions.append( [state, reward, prob[action]] )

            for t in transitions:
                state, reward, prob[action] = t
                pi.put_data((reward, prob[action]))
                print(reward, action)
            # pi.train_net()
            # transitions = []
        elif goal_ob_reward =='finish':
            print('finish')
            transitions.append( [state, reward, prob[action]] )

            for t in transitions:
                state, reward, prob[action] = t
                pi.put_data((reward, prob[action]))
                print(reward, action)
        else:
            print('잘못된 ob_reward')

        state = state_prime
    print(transitions)
    pi.train_net()
    max_cum_reward = max_cum_reward if max_cum_reward > cumul else cumul
    print('▶▶▶ ',epi, 'max cum reward', max_cum_reward, 'isFinished', isFinished, '\n\n')


    #########################################
    if len(env.actions) > 5:
        f.write(str(epi)+'/'+str(items)+'/'+str(cumul)+'/'+str(isFinished)+'\n')
        f.write(str(env.actions))
        f.write('\n')

f.close()
#########################################
