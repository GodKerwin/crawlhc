
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

html_cont = '''
    <!DOCTYPE html>
<html lang="zh-cn" class="no-js">
<head>
<meta http-equiv="Content-Type">
<meta charset="GBK">
<title>慧聪制药工业行业资讯 -慧聪网</title>
<meta name="keywords" content="慧聪制药工业行业资讯,制药工业行业资讯,慧聪网行业资讯"/>
<meta name="description" content="慧聪制药工业行业资讯信息，最新、最全面的制药工业行业资讯报道尽在慧聪网制药工业行业资讯！"/>
<meta name="applicable-device" content="mobile">
<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
<meta name="format-detection" content="telephone=no">
<meta name="format-detection" content="email=no">
<link rel="stylesheet" type="text/css" href="//style.org.hc360.com/css/M-hc/mIndex/global.css"/>
<link rel="stylesheet" type="text/css" href="//style.org.hc360.com/css/M-hc/footer.css"/>
<link rel="stylesheet" type="text/css" href="//style.org.hc360.com/css/M-hc/info/newsStyle.css" />
<link rel="stylesheet" type="text/css" href="//style.org.hc360.com/css/M-hc/seo/mSeoStyle.css"/>
<script src="//style.org.hc360.com/m/source/base/js/zepto.js"></script>
<script src="//style.org.hc360.com/m/source/widgets/iscroll.min.js"></script>
<script src="//style.org.hc360.com/js/build/source/core/jquery.min.js" type="text/javascript"></script>
<script type="text/javascript" src="//style.org.hc360.com/js/M-hc/mIndex/loginCommand.js"></script>
</head>

<body class="BgEc">
	<script type="text/javascript">
			var cpro_id="u2268737";
				(window["cproStyleApi"] = window["cproStyleApi"] || {})[cpro_id]={at:"3",pat:"21",ptLH:"30",tn:"template_inlay_all_mobile_lu_native",rss1:"#FFFFFF",titFF:"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91",titFS:"12",rss2:"#000000",ptFS:"16",ptFC:"#000000",ptFF:"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91",ptFW:"0",conpl:"0",conpr:"1",conpt:"0",conpb:"5",cpro_h:"120",ptn:"1",ptp:"0",itecpl:"10",piw:"0",pih:"0",ptDesc:"2",ptLogo:"0"}
	</script>
	<script src="//cpro.baidustatic.com/cpro/ui/cm.js" type="text/javascript"></script>
<link rel="stylesheet" type="text/css" href="//style.org.hc360.com/css/M-hc/header.css"/>
<script type="text/javascript">
$(function(){
	
	Zepto(".topMoreNew").click(function(){
		$(".topAlertNew").toggle(); 
	})
	Zepto(".topAlertNew a").click(function(){
		$(".topAlertNew").hide(); 
	})
	$(document).on('click touchend',function(event){
		if($(event.target).hasClass("topMoreNew")||$(event.target).closest("div").hasClass("topAlertNew")){
			return;
		}
		$(".topAlertNew").hide();
	});
	
})
</script>

<section class="HeaderBox3" id="headBox" data-query="head">
	<a id='back-pre'  href="javascript:history.go(-1)" class="leftArrow"></a>
    <div class="seaBoxNew">
        <em></em>
        <input type="text" readonly="readonly" placeholder="请输入关键词搜索">
    </div>
    <a class="topMoreNew"></a>
    <a id="bhcMyBtn"  href="https://mlogin.hc360.com/login.html?flag=m" class="hcMyBtn">登录</a>
    <div class="topAlertNew" style="display:none;">
        <em></em>
        <ul>
        		<li><a href="//m.hc360.com/">首页</a></li>
                <li><a href="//m.hc360.com/list/" onclick="sendUserlogsElement('UserBehavior_m_homepage_category_rt');">分类</a></li>
                <li><a href="javascript:void(0)" onclick="javascript:window.location.href='//m.hc360.com/index/inquery.html?flag=m&url='+window.location.href;sendUserlogsElement('UserBehavior_m_homepage_purchase_rt');">采购</a></li>
            </ul>
    </div>
</section>

<script>
Zepto(".seaBoxNew").click(function(){
	window.location.href="//m.hc360.com/search/"; 
})
</script><section>
        <div class="BoxTitle">
            <h3>制药工业行业资讯栏目</h3>
        </div>
        <div class="ListBox2">
        <dl>
        	        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-1.html" title="资讯中心"><span>资讯中心</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-001-1.html" title="精彩推荐"><span>精彩推荐</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-003-1.html" title="健康动态"><span>健康动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-004-1.html" title="国内动态"><span>国内动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-005-1.html" title="国际动态"><span>国际动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-007-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-016-1.html" title="早九点"><span>早九点</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-022-1.html" title="首页要闻推荐(16字)"><span>首页要闻推荐(16字)</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-023-1.html" title="下午茶"><span>下午茶</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-024-1.html" title="产品导购"><span>产品导购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-025-1.html" title="慧聪活动"><span>慧聪活动</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-025-001-1.html" title="十佳评选"><span>十佳评选</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-025-002-1.html" title="本网动态"><span>本网动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-025-003-1.html" title="合作媒体"><span>合作媒体</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-028-1.html" title="医疗动态"><span>医疗动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-031-1.html" title="会员动态 "><span>会员动态 </span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-032-1.html" title="技术交流"><span>技术交流</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-035-1.html" title="高清焦点图幻灯片（新）"><span>高清焦点图幻灯片（新）</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-036-1.html" title="《制药视界》"><span>《制药视界》</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-1.html" title="产品导购汇总"><span>产品导购汇总</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-001-1.html" title="制药装备导购"><span>制药装备导购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-002-1.html" title="医药包装材料导购"><span>医药包装材料导购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-003-1.html" title="中药材成品药导购"><span>中药材成品药导购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-004-1.html" title="医疗器械保健品导购"><span>医疗器械保健品导购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-038-005-1.html" title="药用原辅料"><span>药用原辅料</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-039-1.html" title="药企并购"><span>药企并购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-040-1.html" title="制药工程"><span>制药工程</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-041-1.html" title="药厂工程"><span>药厂工程</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-042-1.html" title="企业推荐"><span>企业推荐</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001001-043-1.html" title="活动推荐"><span>活动推荐</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001002-1.html" title="技术文章"><span>技术文章</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-1.html" title="公告通告"><span>公告通告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-002-1.html" title="药品注册"><span>药品注册</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-002-001-1.html" title="药品行政保护"><span>药品行政保护</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-002-002-1.html" title="中药保护品种"><span>中药保护品种</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-003-1.html" title="药品安全"><span>药品安全</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-003-001-1.html" title="GMP认证公告"><span>GMP认证公告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-003-002-1.html" title="GMP认证审查公告"><span>GMP认证审查公告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-003-005-1.html" title="不良反应"><span>不良反应</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-004-1.html" title="药品市场"><span>药品市场</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-004-001-1.html" title="GSP认证公告"><span>GSP认证公告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-004-002-1.html" title="药品质量公报"><span>药品质量公报</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001004-004-004-1.html" title="GSP认证公示公告"><span>GSP认证公示公告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001010-1.html" title="制药原创新"><span>制药原创新</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001011-1.html" title="慧聪访谈"><span>慧聪访谈</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-1.html" title="月月3.15"><span>月月3.15</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-001-1.html" title="产品质量"><span>产品质量</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-002-1.html" title="假冒产品"><span>假冒产品</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-003-1.html" title="违法广告"><span>违法广告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-004-1.html" title="不良反应"><span>不良反应</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-005-1.html" title="违规失信"><span>违规失信</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001012-006-1.html" title="致病风险"><span>致病风险</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-1.html" title="原料药专区"><span>原料药专区</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-016-1.html" title="技术动态"><span>技术动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-017-1.html" title="企业动态"><span>企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-018-1.html" title="标准法规"><span>标准法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-019-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-020-1.html" title="最新报价"><span>最新报价</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-021-1.html" title="原料药海外动态"><span>原料药海外动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-022-1.html" title="市场分析"><span>市场分析</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-029-1.html" title="植物提取物"><span>植物提取物</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-030-1.html" title="中药材"><span>中药材</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-032-1.html" title="产品动态"><span>产品动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-032-001-1.html" title="医药原料药"><span>医药原料药</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-032-002-1.html" title="天然药物"><span>天然药物</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001014-032-005-1.html" title="生物技术"><span>生物技术</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-1.html" title="制药机械专区"><span>制药机械专区</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-001-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-002-1.html" title="技术动态"><span>技术动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-003-1.html" title="标准法规"><span>标准法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-005-1.html" title="企业动态"><span>企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-1.html" title="产品动态"><span>产品动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-001-1.html" title="原料药机械"><span>原料药机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-002-1.html" title="制剂机械"><span>制剂机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-003-1.html" title="饮片机械"><span>饮片机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-004-1.html" title="药用粉碎机械"><span>药用粉碎机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-005-1.html" title="制药用水设备"><span>制药用水设备</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-006-1.html" title="药品包装机械"><span>药品包装机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-007-1.html" title="药物检测设备"><span>药物检测设备</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-008-1.html" title="其他制药机械"><span>其他制药机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-009-1.html" title="滤芯"><span>滤芯</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-006-010-1.html" title="干燥设备"><span>干燥设备</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001015-007-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-1.html" title="政策法规"><span>政策法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-001-1.html" title="政策要闻"><span>政策要闻</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-002-1.html" title="政策解读"><span>政策解读</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-004-1.html" title="药监动态"><span>药监动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-005-1.html" title="法规文件"><span>法规文件</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-005-001-1.html" title="药品市场"><span>药品市场</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-005-002-1.html" title="注册生产"><span>注册生产</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001016-005-003-1.html" title="药品安全"><span>药品安全</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-1.html" title="市场分析"><span>市场分析</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-001-1.html" title="药品价格"><span>药品价格</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-002-1.html" title="医药营销"><span>医药营销</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-003-1.html" title="医药进出口"><span>医药进出口</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-004-1.html" title="医药财经"><span>医药财经</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001017-006-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-1.html" title="热点专题"><span>热点专题</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-001-1.html" title="时事·热点"><span>时事·热点</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-002-1.html" title="月月315"><span>月月315</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-003-1.html" title="市场·产品"><span>市场·产品</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-004-1.html" title="展会·活动"><span>展会·活动</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-005-1.html" title="医疗·健康"><span>医疗·健康</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001018-007-1.html" title="热门关键词"><span>热门关键词</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-1.html" title="研究频道"><span>研究频道</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-001-1.html" title="进出口月评"><span>进出口月评</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-002-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-003-1.html" title="产业预警"><span>产业预警</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-004-1.html" title="新药研发"><span>新药研发</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-005-1.html" title="销售研究"><span>销售研究</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-008-1.html" title="主要生产企业动态"><span>主要生产企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-008-001-1.html" title="华北制药"><span>华北制药</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-008-001-003-1.html" title="投资合作"><span>投资合作</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-008-003-1.html" title="哈药"><span>哈药</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-008-003-001-1.html" title="业绩追踪"><span>业绩追踪</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001025-010-1.html" title="研究报告"><span>研究报告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-1.html" title="医药科技"><span>医药科技</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-001-1.html" title="制药工艺"><span>制药工艺</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-002-1.html" title="健康探索"><span>健康探索</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-003-1.html" title="药物研究"><span>药物研究</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-007-1.html" title="新药动态"><span>新药动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001026-008-1.html" title="医学前沿"><span>医学前沿</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-1.html" title="医药包装专区"><span>医药包装专区</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-001-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-002-1.html" title="技术动态"><span>技术动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-003-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-1.html" title="产品动态"><span>产品动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-001-1.html" title="药用塑料类"><span>药用塑料类</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-002-1.html" title="薄膜与复合膜"><span>薄膜与复合膜</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-003-1.html" title="片材与药片类"><span>片材与药片类</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-004-1.html" title="合成纸与无纺布"><span>合成纸与无纺布</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-005-1.html" title="药用玻璃类"><span>药用玻璃类</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-004-006-1.html" title="其他包装材料"><span>其他包装材料</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-005-1.html" title="企业动态"><span>企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001027-006-1.html" title="标准法规"><span>标准法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-1.html" title="企业动态"><span>企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-001-1.html" title="业界人物"><span>业界人物</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-002-1.html" title="股企看台"><span>股企看台</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-003-1.html" title="国际企业"><span>国际企业</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-004-1.html" title="国内企业"><span>国内企业</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-005-1.html" title="成交快讯"><span>成交快讯</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001028-006-1.html" title="成功故事"><span>成功故事</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001029-1.html" title="中药材"><span>中药材</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001029-001-1.html" title="行情"><span>行情</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001029-002-1.html" title="技术"><span>技术</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001029-003-1.html" title="知识"><span>知识</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001029-004-1.html" title="动态"><span>动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001035-1.html" title="医药招标"><span>医药招标</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001035-001-1.html" title="招标采购"><span>招标采购</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001035-001-001-1.html" title="药品耗材"><span>药品耗材</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001035-001-002-1.html" title="器械设备"><span>器械设备</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001035-003-1.html" title="药品耗材中标公告"><span>药品耗材中标公告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-1.html" title="药用辅料专区"><span>药用辅料专区</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-001-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-002-1.html" title="企业动态"><span>企业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-003-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-004-1.html" title="技术动态"><span>技术动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-005-1.html" title="标准法规"><span>标准法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-006-1.html" title="产品动态"><span>产品动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-006-003-1.html" title="崩解剂"><span>崩解剂</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001037-006-007-1.html" title="干燥剂"><span>干燥剂</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-1.html" title="展览会议"><span>展览会议</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-002-1.html" title="展会预告"><span>展会预告</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-003-1.html" title="会议通知"><span>会议通知</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-004-1.html" title="展会报道"><span>展会报道</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-005-1.html" title="会议报道"><span>会议报道</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-006-1.html" title="企业活动"><span>企业活动</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-007-1.html" title="展会服务"><span>展会服务</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001038-008-1.html" title="展馆介绍"><span>展馆介绍</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001039-1.html" title="08终极测试用"><span>08终极测试用</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001040-1.html" title="中国医药行业信息"><span>中国医药行业信息</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001040-002-1.html" title="行业动态"><span>行业动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001040-003-1.html" title="政策解读"><span>政策解读</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001040-004-1.html" title="产业观察"><span>产业观察</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001040-007-1.html" title="营销管理"><span>营销管理</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001041-1.html" title="2009专家在线"><span>2009专家在线</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001041-002-1.html" title="专家最新动态"><span>专家最新动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001041-003-1.html" title="时事点评"><span>时事点评</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001041-004-1.html" title="专家看点"><span>专家看点</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001041-006-1.html" title="协会传真"><span>协会传真</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-1.html" title="多媒体资讯"><span>多媒体资讯</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-001-1.html" title="新闻视点"><span>新闻视点</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-003-1.html" title="塑身馆"><span>塑身馆</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-004-1.html" title="拍案惊奇"><span>拍案惊奇</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-005-1.html" title="美颜坊"><span>美颜坊</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-006-1.html" title="养生堂"><span>养生堂</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-007-1.html" title="饮食汇"><span>饮食汇</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-008-1.html" title="药事曝光"><span>药事曝光</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001042-009-1.html" title="星业秀"><span>星业秀</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-1.html" title="健康专栏"><span>健康专栏</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-001-1.html" title="瘦身宝典"><span>瘦身宝典</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-002-1.html" title="养生新知"><span>养生新知</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-003-1.html" title="用药指南"><span>用药指南</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-004-1.html" title="疾病知识"><span>疾病知识</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-005-1.html" title="营养美食"><span>营养美食</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-006-1.html" title="两性天地"><span>两性天地</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-007-1.html" title="美颜攻略"><span>美颜攻略</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-011-1.html" title="美体秘籍"><span>美体秘籍</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-012-1.html" title="食补禁忌"><span>食补禁忌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001043-013-1.html" title="食疗扮靓"><span>食疗扮靓</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001044-1.html" title="视频采访"><span>视频采访</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-1.html" title="2010人物访谈"><span>2010人物访谈</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-001-1.html" title="专家领导"><span>专家领导</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-002-1.html" title="制药设备企业"><span>制药设备企业</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-003-1.html" title="原辅料企业"><span>原辅料企业</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-004-1.html" title="药用包装企业"><span>药用包装企业</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001045-005-1.html" title="药厂专访"><span>药厂专访</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001046-1.html" title="通讯员供稿"><span>通讯员供稿</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-1.html" title="2013十佳专题直播稿件"><span>2013十佳专题直播稿件</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-1.html" title="获奖企业资讯"><span>获奖企业资讯</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-001-1.html" title="十佳风云人物"><span>十佳风云人物</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-002-1.html" title="十佳用户满意知名品牌"><span>十佳用户满意知名品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-003-1.html" title="十佳新锐知名品牌"><span>十佳新锐知名品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-004-1.html" title="十佳最具诚信知名品牌"><span>十佳最具诚信知名品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-005-1.html" title="十佳最具竞争力知名品牌"><span>十佳最具竞争力知名品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-001-006-1.html" title="十佳民族品牌"><span>十佳民族品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-002-1.html" title="采访企业资讯"><span>采访企业资讯</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-003-1.html" title="奖项列表名单"><span>奖项列表名单</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-004-1.html" title="其他稿件"><span>其他稿件</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001047-005-1.html" title="论坛稿件"><span>论坛稿件</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001048-1.html" title="医疗器械"><span>医疗器械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001048-001-1.html" title="政策法规"><span>政策法规</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001048-002-1.html" title="前沿科技"><span>前沿科技</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001048-003-1.html" title="市场动态"><span>市场动态</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001050-1.html" title="2016年度慧聪食品制药行业品牌盛会"><span>2016年度慧聪食品制药行业品牌盛会</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001050-001-1.html" title="制药工业领军品牌"><span>制药工业领军品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001050-003-1.html" title="制药工业十佳药用辅料品牌"><span>制药工业十佳药用辅料品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001050-004-1.html" title="制药工业十佳用户推荐品牌"><span>制药工业十佳用户推荐品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001050-005-1.html" title="制药工业十佳成长力品牌"><span>制药工业十佳成长力品牌</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001051-1.html" title="2017版首页新闻"><span>2017版首页新闻</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001051-001-1.html" title="1F原料药设备及机械"><span>1F原料药设备及机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001051-002-1.html" title="2F制剂设备及机械"><span>2F制剂设备及机械</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001051-003-1.html" title="3F药用粉碎设备"><span>3F药用粉碎设备</span><em></em></a>
            </dd>
			        	 <dd>
                <a href="//m.hc360.com/info-pharmacy/list/001051-004-1.html" title="首页资讯列表"><span>首页资讯列表</span><em></em></a>
            </dd>
			        </dl>
        </div>
</section>
<section class="areaBox">
	<a href="//m.hc360.com/">慧聪网</a>
	<a href="//m.hc360.com/info/">资讯中心</a>
	<a href="//m.hc360.com/info-pharmacy/list.html">制药工业行业资讯栏目</a>
</section>
<section class="botAd">
	<!-- m站资讯广告 add 2015/10/26 -->
           <script type="text/javascript">
          		var cpro_id="u2375769";
  		(window["cproStyleApi"] = window["cproStyleApi"] || {})[cpro_id]={at:"3",hn:"0",wn:"0",imgRatio:"1.7",scale:"20.7",pat:"6",tn:"template_inlay_all_mobile_lu_native",rss1:"#FFFFFF",adp:"1",ptt:"0",titFF:"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91",titFS:"14",rss2:"#000000",titSU:"0",ptbg:"70",ptp:"0"}
</script>
<script src="//cpro.baidustatic.com/cpro/ui/cm.js" type="text/javascript"></script>
</section>
<link href="//style.org.hc360.com/css/M-hc/newheader.css" rel="stylesheet" type="text/css">
<footer class="pBottom">
<section class="botBox">
    <p class="loginBox" data-query="commonLoginFoot">
    <a href="https://mlogin.hc360.com/login.html?flag=m" rel="nofollow" class="log">登录</a>
    <a href="https://mlogin.hc360.com/reg.html?flag=m" rel="nofollow" class="reg">注册</a>
    </p>
    <p class="txt1"><a href="//js.hc360.com/">极速版</a><span>|</span><a href="//www.hc360.com/?ads=m">电脑版</a><span>|</span><a href="//m.hc360.com/cp/">微门户</a><span>|</span><a href="//m.hc360.com/category/">导航</a><span>|</span><a href="//m.hc360.com/help/">帮助</a></p>
	<p class="txt2">慧聪网 版权所有 &copy;2018 Hc360.com</p>
	<div class="botRight">
		<a rel="nofollow"  href="//m.hc360.com/history/store.html" class="hosRight" id="hosRight" style="display:none"></a>
	
	    <a href="javascript:scroll(0,0)" class="fbackTop" id="fTopBox" style="display: none;"></a>
	</div>
</section>
     <section class="botHwj">
        <a href="https://author.baidu.com/home/1573321233077508?from=dusite_artdetailh5" onclick="sendUserlogsElement('UserBehavior_m_author_baidu_bar')">进入熊掌号</a>
    </section>
</footer>
<a  rel="nofollow"   href="javascript:void(0)" onclick="javascript:window.location.href='//m.hc360.com/index/inquery.html?flag=m&mtype=102&flag=m&url='+window.location.href;sendUserlogsElement('UserBehavior_m_cp_purchase?detailuserid=&detailbcid=');" class="fPurchase" id="fPurchase1" >采购</a>
<script>

var index = $('.areaBox a').length - 2;
var text = $('.areaBox a:eq('+index+')').attr('href');
$('#back-pre').attr({href:text});


$(function(){
	window.onscroll = function () {
	if (document.documentElement.scrollTop + document.body.scrollTop > 100) {
		document.getElementById("fTopBox").style.display = "block";
		if(document.getElementById("fPurchase1")){
			document.getElementById("fPurchase1").style.display = "block";
		}
		if(document.getElementById("hosRight")){
			document.getElementById("hosRight").style.display = "block";
		}
	}
	else {
		document.getElementById("fTopBox").style.display = "none";
		if(document.getElementById("fPurchase1")){
			document.getElementById("fPurchase1").style.display = "none";
		}
		if(document.getElementById("hosRight")){
			document.getElementById("hosRight").style.display = "none";
		}
}
}
})
</script><script src="//style.org.hc360.com/m/source/base/js/performace.js"></script>
</body>
<script> 
var _hmt = _hmt || []; 
(function() { 
var hm = document.createElement("script"); 
hm.src = "//hm.baidu.com/hm.js?3eb870aae8a6d70d3c563aef859c8d37"; 
var s = document.getElementsByTagName("script")[0]; 
s.parentNode.insertBefore(hm, s); 
})(); 
</script>
</html>
'''
soup = BeautifulSoup(html_cont, 'html.parser')
print(soup)
urls = soup.select('section > div.ListBox2 > dl > dd > a')
result = [[url.text, urljoin('https://m.hc360.com/info-pharmacy/list.html', url.get('href'))] for url in urls]
i = 1
for item in result:
    print(i, item[0], item[1])
    i += 1
