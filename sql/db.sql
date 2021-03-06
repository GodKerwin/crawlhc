-- ----------------------------
-- Create DB for db_news
-- ----------------------------
# CREATE DATABASE `zx` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use zx;

-- ----------------------------
-- Table structure for crawl_category
-- ----------------------------
DROP TABLE IF EXISTS `crawl_category`;
CREATE TABLE `crawl_category` (
  `pid` int(11) NOT NULL COMMENT '一级类目ID',
  `cid` int(11) NOT NULL COMMENT '二级分类ID',
  `name`  varchar(32) NOT NULL DEFAULT '' COMMENT '类目名称' ,
  `link`  varchar(200) NOT NULL DEFAULT '' COMMENT '链接' ,
  PRIMARY KEY (`pid`, `cid`),
  UNIQUE KEY (`link`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='类目表';

-- ----------------------------
-- Table structure for crawl_news
-- ----------------------------
DROP TABLE IF EXISTS `crawl_news`;
CREATE TABLE `crawl_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `pid` int(11) NOT NULL COMMENT '一级类目ID',
  `cid`  int(11) NOT NULL COMMENT '二级分类ID' ,
  `title`  varchar(200) NOT NULL DEFAULT '' COMMENT '标题' ,
  `content` text COMMENT '内容' ,
  `link` varchar(500) NOT NULL DEFAULT '' COMMENT '链接' ,
  `createAt` int(10) NOT NULL DEFAULT 0 COMMENT '入库时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`link`),
  KEY `category` (`pid`,`cid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='资讯表';

-- ----------------------------
-- Table structure for crawl_recommend
-- ----------------------------
# DROP TABLE IF EXISTS `crawl_recommend`;
# CREATE TABLE `crawl_recommend` (
#   `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
#   `category` varchar(32) NOT NULL DEFAULT '' COMMENT '主分类',
#   `subcategory`  varchar(32) NOT NULL DEFAULT '' COMMENT '二级分类' ,
#   `title`  varchar(200) NOT NULL DEFAULT '' COMMENT '标题' ,
#   `content` text COMMENT '内容' ,
#   `link` varchar(500) NOT NULL DEFAULT '' COMMENT '链接' ,
#   `createAt` int(10) NOT NULL DEFAULT 0 COMMENT '入库时间',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY (`link`),
#   KEY `category` (`category`,`subcategory`) USING BTREE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='推荐表';