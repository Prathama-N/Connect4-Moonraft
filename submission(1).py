def my_agent(observation, configuration):
    from random import choice
    # 从一个给定的可迭代对象中随机选择一个元素 从一个列表中选择一个满足条件的元素
    # choice() 函数选择的就是满足条件 observation.board[c] == 0 的随机元素
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
