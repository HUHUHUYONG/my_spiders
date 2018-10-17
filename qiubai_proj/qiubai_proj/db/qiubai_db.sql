
CREATE TABLE `qiubai` (
  `id`  int(11) PRIMARY  KEY  auto_increment COMMENT '自增主键',
  `image_url` VARCHAR(300) COMMENT  '图片地址',
  `name` VARCHAR(50) COMMENT '名称',
  `sex`  VARCHAR(10) COMMENT '性别',
  `age`  VARCHAR(10) COMMENT '年龄',
  `content` VARCHAR(500) COMMENT '内容',
  `image_figer` VARCHAR(100) COMMENT '照片指纹'
)ENGINE=InnoDB DEFAULT charset=utf8;