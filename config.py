import os
from log import Log
logger = Log()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'some string'
    APP_NAME = 'cft'
    MONGODB_SETTINGS = {'DB': 'cft'}


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True


class ProductionConfig(Config):
    """生产环境配置"""
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
