import pygame


class Role:
    def __init__(self, screen):
        """初始化飞船并设置七初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/贞德.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.center = self.screen_rect.center
        # self.rect.center =self.screen_rect.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
