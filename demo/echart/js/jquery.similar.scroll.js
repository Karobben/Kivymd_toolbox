(function ($) {
    $.fn.scroll = function (options) {
        var root = this,                // 将当前上下文对象存入root
            timer = [],                 // 计时器
            // ulTag = $("> ul", root), // ul标签
            // liTag = $("> li", ulTag),// li标签(集合)
            ulTag = root,    //ul标签
            liTag = $("> div", ulTag),  // li标签(集合)
            liNum = liTag.length,       // li标签个数
            liOne = liTag.first(),      // 获取单个li标签
            marquee,                    // 滚动器(函数)
            liUnit,                     // 单个li的宽或者高(横向时为宽，纵向时为高)
            ulUnit,                     // ul的宽或者高(横向时为宽，纵向时为高)
            limit,                      // root的宽或者高(横向时为宽，纵向时为高)
            cssName,                    // 样式名称(横向时为margin-left，纵向时为margin-top)
            effect;                     // 动画效果(横向时为marginLeft，纵向时为marginTop)

        // 默认配置
        var settings = {
            speed: 40,      // 滚动速度,值越大速度越慢
            direction: "x"  // 滚动方向("x"或者"y" [x横向;y纵向])
        };

        // 不为空，则合并参数
        if (options) {
            $.extend(settings, options);
        }

        // 横向
        if (settings.direction === "x") {
            limit = root.width();
            cssName = "margin-left";
            liUnit = liOne.outerWidth(true);
            ulUnit = liUnit * liNum;            // 单个li的宽 ＊ li的个数 ＝ ul的宽度
            effect = { marginLeft : "-=1" };

            ulTag.css({ width: ulUnit });       // 设置ul的宽
        }

        // 纵向
        if (settings.direction === "y") {
            limit = root.height();
            cssName = "margin-top";
            liUnit = liOne.outerHeight(true);
            ulUnit = liUnit * liNum;            // 单个li的高 ＊ li的个数 ＝ ul的高度
            effect = { marginTop : "-=1" };
           
            ulTag.css({ height: ulUnit });      // 设置ul的高
        }

        marquee = function() {
            ulTag.animate(effect, 0, function() {

                // ul滚动的距离，取绝对值
                var distance = Math.abs(parseInt($(this).css(cssName),10));

                // 如果滚动的距离一旦大于单个li的长度
                if (distance > liUnit) {
                    $("> li:first", $(this)).appendTo($(this)); // 就把第一个li移到最后
                    $(this).css(cssName, 0);                    // 滚动长度归0
                }
            })
        }

        // 遵循链式原则，并进行初始化
        return root.each(function (i) {
            // 只有当ul的长度大于root长度时才进行滚动
            if (ulUnit > limit) {               
                timer[i] = setInterval(marquee,settings.speed);

                // 鼠标进入停止滚动，离开继续滚动
                $(this).hover(function () {
                    clearInterval(timer[i]);
                }, function () {
                    timer[i] = setInterval(marquee,settings.speed);
                })
            }
        })
    };
})(jQuery);