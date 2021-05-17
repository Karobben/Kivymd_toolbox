// 地图容器
var chart = echarts.init(document.getElementById('map'));

// 34个省、市、自治区的名字拼音映射数组
var provinces = {
    // 23个省
    "台湾": "taiwan",
    "河北": "hebei",
    "山西": "shanxi",
    "辽宁": "liaoning",
    "吉林": "jilin",
    "黑龙江": "heilongjiang",
    "江苏": "jiangsu",
    "浙江": "zhejiang",
    "安徽": "anhui",
    "福建": "fujian",
    "江西": "jiangxi",
    "山东": "shandong",
    "河南": "henan",
    "湖北": "hubei",
    "湖南": "hunan",
    "广东": "guangdong",
    "海南": "hainan",
    "四川": "sichuan",
    "贵州": "guizhou",
    "云南": "yunnan",
    "陕西": "shanxi1",
    "甘肃": "gansu",
    "青海": "qinghai",
    // 5个自治区
    "新疆": "xinjiang",
    "广西": "guangxi",
    "内蒙古": "neimenggu",
    "宁夏": "ningxia",
    "西藏": "xizang",
    // 4个直辖市
    "北京": "beijing",
    "天津": "tianjin",
    "上海": "shanghai",
    "重庆": "chongqing",
    // 2个特别行政区
    "香港": "xianggang",
    "澳门": "aomen"
};

// 直辖市和特别行政区-只有二级地图，没有三级地图
var special = ["北京","天津","上海","重庆","香港","澳门"];
var mapdata = []; // 全国地图数据
var provinceVal = ""; // 选中的省份;
var provinceNumber = []; // 省份的编号
var cityVal = ""; // 选中的市
var areaVal = ""; // 选中的区
var address = ""; // 经纬度位置
var selectMold = null; // 选择的类型 （0省份、1直辖市或特别行政区）
var selectRank = null; // 选择的类别 （0市、1区）
var locationName = ""; // 位置名称

// 绘制全国地图
$.getJSON('./map/china.json', function(data) {
	var d = [];
	for (var i = 0;i < data.features.length;i++) {
		d.push({name: data.features[i].properties.name});
	}
	mapdata = d;
    provinceNumber = data;
	echarts.registerMap('china', data); // 注册地图
	renderMap('china', d); // 绘制地图
});

// 地图点击事件
chart.on('click', function (params) {
    $(".goback").removeClass("hide"); // 显示返回按钮
	if (params.name in provinces) {
		// 如果点击的是34个省、市、自治区，绘制选中地区的二级地图
		$.getJSON('./map/province/'+ provinces[params.name] +'.json', function(data) {
			echarts.registerMap(params.name, data);
			var d = [];
			for (var i = 0;i < data.features.length;i++) {
				d.push({name:data.features[i].properties.name});
			}
            provinceVal = params.name+"省"; // 当前选中的省份
			renderMap(params.name, d); // 绘制地图
            if (special.indexOf(params.name) >= 0) {
                selectMold = 1; // 自治区
            } else {
                selectMold = 0; // 省份
            }
		});
	} else if (params.seriesName in provinces) {
		// 如果是【直辖市/特别行政区】只有二级下钻
		if (special.indexOf(params.seriesName) >= 0) {
            address = params.seriesName + params.name; 
            showMap(address); // 调起高德地图
            selectRank = 1;
            locationName = params.name; // 位置名称
		} else {
			// 显示县级地图
			$.getJSON('./map/city/'+ cityMap[params.name] +'.json', function(data) {
				echarts.registerMap(params.name, data);
				var d = [];
				for (var i = 0;i < data.features.length;i++) {
					d.push({name: data.features[i].properties.name});
				}
                cityVal = params.name; // 当前选中的市
				renderMap(params.name, d); // 绘制地图
			})
            selectRank = 0;
		}
	} else {
        areaVal = params.name; 
        address = provinceVal + cityVal + areaVal; 
        showMap(address); // 调起高德地图
        selectRank = 1;
        locationName = areaVal; // 位置名称
	}
});

/**
 * 返回按钮点击事件
 */
$(".goback").on('click', function (e) {
    if (selectMold == 0) {
        // 省份
        if (selectRank == 1) { // 区
            $("#gouldMap").addClass("hide");
            $("#map").removeClass("hide");
            selectRank = 0;
        } else if (selectRank == 0) { // 市
            var tempStr = provinceVal.substring(0, provinceVal.length - 1);
            if (tempStr in provinces) {
                // 如果点击的是34个省、市、自治区，绘制选中地区的二级地图
                $.getJSON('./map/province/'+ provinces[tempStr] +'.json', function(data) {
                    echarts.registerMap(tempStr, data);
                    var d = [];
                    for (var i = 0;i < data.features.length;i++) {
                        d.push({name:data.features[i].properties.name});
                    }
                    renderMap(tempStr, d); // 绘制地图
                });
                selectRank = null;
            }
        } else { // 省
            $(".goback").addClass("hide"); // 显示返回按钮
            echarts.registerMap('china', provinceNumber); // 注册地图
            renderMap('china', mapdata); // 绘制地图    
        } 
    } else if (selectMold == 1) {
        // 直辖市或特别行政区
        if (selectRank == 1) { // 区
            $("#gouldMap").addClass("hide");
            $("#map").removeClass("hide");
            selectRank = null;
        } else {
            $(".goback").addClass("hide"); // 显示返回按钮
            echarts.registerMap('china', provinceNumber); // 注册地图
            renderMap('china', mapdata); // 绘制地图    
        }
    }
})

/**
 * 显示高德地图
 */
var showMap = function(location) {
    var url = "http://restapi.amap.com/v3/geocode/geo?key=c5275afb9258f34314bdbe23067c203d&s=rsv3&city=35&address="+location;
    var cityCode = ""; // 城市编码
    $.ajax({
        url: "./map/cityCode.json",
        type: "GET",
        data: "",
        async: false, 
        contentType: "text/json,charset=utf-8",
        dataType: "json",
        success: function(data) {
            if (data.length) {
                for (var i = 0;i < data.length;i++) {
                    if (data[i]['name'] == locationName) {
                        cityCode = data[i]["code"]; 
                        console.log(cityCode);
                        return false;
                    }
                    console.log(data[i]['name']);
                }
            } 
        },
        error: function(error) {
            console.log(error);
        }
    })
    $.getJSON(url, function(data) {
        if (parseInt(data.status)) {
            var locationStr = data.geocodes[0]['location']; // 经纬度
            var lat = locationStr.split(",")[0];
            var lon = locationStr.split(",")[1];
            var map = new AMap.Map('gouldMap', {
                resizeEnable: true, // 是否监控地图容器尺寸变化
                zoom: 18, // 初始化地图层级
                center: [lat, lon], // 初始化地图中心点
                // viewMode: '3D',// 使用3D视图
                // pitch: 45
            });
            var markers = [];
            var positions = [[116.4, 39.9], [116.4, 39.9], [116.4, 39.9], [116.4, 39.9],[116.3, 39.9]];
            for (var i = 0; i < positions.length; i++) {
                var marker = new AMap.Marker({
                    map: map,
                    position: positions[i],
                    offset: new AMap.Pixel(-10, 20)
                });
                var str = "经纬度为："+ positions[i];
                var text = new AMap.Text({text: str, textAlign: 'center', verticalAlign: 'middle', draggable: false, cursor: 'pointer', position: positions[i]});
                text.setMap(map);
                markers.push(marker);
            }
            $("#map").addClass("hide");
            $("#gouldMap").removeClass("hide");
        }
    })
};


// 初始化绘制全国地图配置
var option = {
	backgroundColor: 'rgba(255, 255, 255, 0)',
    title : {
        text: '',
        subtext: '三级下钻',
        // link: 'https://blog.csdn.net/example440982',
        link: '',
        left: 'center',
        textStyle:{
            color: '#fff',
            fontSize: 16,
            fontWeight: 'normal',
            fontFamily: "Microsoft YaHei"
        },
        subtextStyle:{
        	color: '#ccc',
            fontSize:13,
            fontWeight: 'normal',
            fontFamily: "Microsoft YaHei"
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}'
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        // feature: {
        //     dataView: {readOnly: false},
        //     restore: {},
        //     saveAsImage: {}
        // },
        iconStyle: {
        	normal: {
        		color: '#fff'
        	}
        }
    },
    animationDuration: 1000,
	animationEasing: 'cubicOut',
	animationDurationUpdate: 1000
     
};

/**
 * 城市地图下钻渲染
 */
function renderMap(map,data) {
	option.title.subtext = map;
    option.series = [ 
		{
            name: map,
            type: 'map',
            mapType: map,
            roam: false,
            nameMap:{
			    'china': '中国'
			},
            label: {
	            normal:{
					show: true,
					textStyle: {
						color: '#999',
						fontSize: 13
					}  
	            },
	            emphasis: {
	                show: true,
	                textStyle: {
						color: '#fff',
						fontSize: 13
					}
	            }
	        },
	        itemStyle: {
	            normal: {
	                areaColor: '#323c48',
	                borderColor: 'dodgerblue'
	            },
	            emphasis: {
	                areaColor: 'darkorange'
	            }
	        },
            data: data
        }	
    ];
    // 渲染地图
    chart.setOption(option);
}