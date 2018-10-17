# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/11 下午4:38'
import json
from twisted.enterprise import adbapi
from .settings import MYSQL_SETTINGS
import logging


class MySQLPipeLine(object):
    def __init__(self, dbpool):
        self.__dbpool = dbpool

    @classmethod
    def from_crawler(cls, settings):
        # 读取配置文件内容
        dbparams = dict(
            host=MYSQL_SETTINGS['HOST'],
            db=MYSQL_SETTINGS['DATABASE'],
            user=MYSQL_SETTINGS['USER'],
            passwd=MYSQL_SETTINGS['PASSWORD'],
            charset=MYSQL_SETTINGS['CHARSET'],
        )
        # 创建mysql连接池
        dbpool = adbapi.ConnectionPool("pymysql", **dbparams) #**进行解包
        return cls(dbpool)

    def process_item(self, item, spider):
        '''
        使用twisted提供的adbapi接口处理item数据
        :param item: 从spiders通过yield发送过来数据
        :param spider: 从spiders里面选取的spider
        :return:
        '''
        if item['t_name']:
            defferd = self.__dbpool.runInteraction(self.db_insert_handle, item)
            # defferd.addErrback(self.db_insert_error_handle, item, spider)

        # TODO, 如果要加入其它db操作
        # TODO: defferd = self.__dbpool.runInteraction(self.db_update_handle, item)
        # TODO  defferd.addErrback(self.db_error_handle, item, spider)

        return item

    def db_insert_error_handle(self, failure, item, spider):
        '''
        处理db操作异常情况
        :param failure:  异常错误信息
        :param item:
        :param spider:
        :return:
        '''
        logging.error(f"db_error_handle has error with {item}")

    def db_insert_handle(self, cursor, item):
        '''
        操作item，具体将item数据插入db
        :param cursor:
        :param item:
        :return:
        '''

        # logging.info(f"insert data: {item}")

        insert_sql = """
						 insert into tag
						 VALUES(%s, %s, %s, %s, %s)
					 """
        item_values = (item['id'], item['t_name'], item['t_info'],
                       item['t_createtime'], item['t_flag'])
        cursor.execute(insert_sql, item_values)

        return True

