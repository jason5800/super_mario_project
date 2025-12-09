import gym
import gym_super_mario_bros
from gym.wrappers import RecordVideo
import cv2
import numpy as np

class BackgroundRemoveWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        # ... 重新定义observation_space，例如变为灰度或二值化后的空间 ...

    def observation(self, frame):
        # 定义蓝色的范围（这些阈值需要根据具体游戏画面调整）
        background = np.array([104, 136, 252]) # 背景色
        # 创建掩膜，所有在蓝色范围内的像素变为255（白色），其他为0（黑色）
        mask = cv2.inRange(frame, background-1, background+1)
        # 将原图中非蓝色的部分保留，蓝色的部分置为黑色（或其他背景色）
        frame[mask > 0] = 0

        # 云朵等
        low_cloud = np.array([250, 250, 250]) # 低云颜色
        high_cloud = np.array([255, 255, 255]) # 高云颜色
        # 创建掩膜，所有在低云高云范围内的像素变为255（白色），其他为0（黑色）
        mask_cloud = cv2.inRange(frame, low_cloud, high_cloud)
        # 将原图中非低云高云的部分保留，低云高云置为黑色（或其他背景色）
        frame[mask_cloud > 0] = 0

        return frame

# 创建环境并指定渲染模式
env = gym_super_mario_bros.make("SuperMarioBros-1-3-v0")  # 使用rgb_array模式进行视频录制
# 应用视频录制包装器
# env = RecordVideo(env, video_folder="./mario_videos", episode_trigger=lambda x: x % 10 == 0) # 每100回合录制一次

observation = env.reset()
print(observation.shape)
print(observation.dtype)

# obs_numpy = np.array(observation)
obs_bgr = cv2.cvtColor(observation, cv2.COLOR_RGB2BGR)
cv2.imwrite("observation.png", obs_bgr)

env_adjust = BackgroundRemoveWrapper(env)
observation_adjust = env_adjust.reset()

obs_adjust_bgr = cv2.cvtColor(observation_adjust, cv2.COLOR_RGB2BGR)
cv2.imwrite("observation_adjust.png", obs_adjust_bgr)



env.close()