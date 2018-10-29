
e9f.data = k9b.cH0x({
                params: bZB3x.encText,
                encSecKey: bZB3x.encSecKey
            })


var bZB3x = window.asrsea(JSON.stringify(i9b), bnY2x(["流泪", "强"]), bnY2x(ZQ8I.md), bnY2x(["爱心", "女孩", "惊恐", "大笑"]));


!function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();

可以看到window.asrsea = d,而d是个什么玩意呢？

function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }


参数分别为：
JSON.stringify(i9b)
bnY2x(["流泪", "强"])
bnY2x(ZQ8I.md)
bnY2x(["爱心", "女孩", "惊恐", "大笑"])

i9b = {
        "大笑": "86",
        "可爱": "85",
        "憨笑": "359",
        "色": "95",
        "亲亲": "363",
        "惊恐": "96",
        "流泪": "356",
        "亲": "362",
        "呆": "352",
        "哀伤": "342",
        "呲牙": "343",
        "吐舌": "348",
        "撇嘴": "353",
        "怒": "361",
        "奸笑": "341",
        "汗": "97",
        "痛苦": "346",
        "惶恐": "354",
        "生病": "350",
        "口罩": "351",
        "大哭": "357",
        "晕": "355",
        "发怒": "115",
        "开心": "360",
        "鬼脸": "94",
        "皱眉": "87",
        "流感": "358",
        "爱心": "33",
        "心碎": "34",
        "钟情": "303",
        "星星": "309",
        "生气": "314",
        "便便": "89",
        "强": "13",
        "弱": "372",
        "拜": "14",
        "牵手": "379",
        "跳舞": "380",
        "禁止": "374",
        "这边": "262",
        "爱意": "106",
        "示爱": "376",
        "嘴唇": "367",
        "狗": "81",
        "猫": "78",
        "猪": "100",
        "兔子": "459",
        "小鸡": "450",
        "公鸡": "461",
        "幽灵": "116",
        "圣诞": "411",
        "外星": "101",
        "钻石": "52",
        "礼物": "107",
        "男孩": "0",
        "女孩": "1",
        "蛋糕": "337",
        18: "186",
        "圈": "312",
        "叉": "313"
    }


var bnY2x = function(cQv6p) {
        var m9d = [];
        k9b.bf9W(cQv6p, function(cQt6n) {
            m9d.push(ZQ8I.emj[cQt6n])
        });
        return m9d.join("")
    };

k9b.bf9W = function(j9a, cL0x, O9F) {
        if (!j9a || !j9a.length || !k9b.hl2x(cL0x))
            return this;
        if (!!j9a.forEach) {
            j9a.forEach(cL0x, O9F);
            return this
        }
        for (var i = 0, l = j9a.length; i < l; i++)
            cL0x.call(O9F, j9a[i], i, j9a);
        return this
    };

ZQ8I = c9h("nm.x.ek")
var c9h = NEJ.P
NEJ.P = function(DC9t) {
        if (!DC9t || !DC9t.length)
            return null;
        var bbR7K = window;
        for (var a = DC9t.split("."), l = a.length, i = a[0] == "window" ? 1 : 0; i < l; bbR7K = bbR7K[a[i]] = bbR7K[a[i]] || {},
        i++)
            ;
        return bbR7K
    }

ZQ8I.emj = {
        "色": "00e0b",
        "流感": "509f6",
        "这边": "259df",
        "弱": "8642d",
        "嘴唇": "bc356",
        "亲": "62901",
        "开心": "477df",
        "呲牙": "22677",
        "憨笑": "ec152",
        "猫": "b5ff6",
        "皱眉": "8ace6",
        "幽灵": "15bb7",
        "蛋糕": "b7251",
        "发怒": "52b3a",
        "大哭": "b17a8",
        "兔子": "76aea",
        "星星": "8a5aa",
        "钟情": "76d2e",
        "牵手": "41762",
        "公鸡": "9ec4e",
        "爱意": "e341f",
        "禁止": "56135",
        "狗": "fccf6",
        "亲亲": "95280",
        "叉": "104e0",
        "礼物": "312ec",
        "晕": "bda92",
        "呆": "557c9",
        "生病": "38701",
        "钻石": "14af6",
        "拜": "c9d05",
        "怒": "c4f7f",
        "示爱": "0c368",
        "汗": "5b7a4",
        "小鸡": "6bee2",
        "痛苦": "55932",
        "撇嘴": "575cc",
        "惶恐": "e10b4",
        "口罩": "24d81",
        "吐舌": "3cfe4",
        "心碎": "875d3",
        "生气": "e8204",
        "可爱": "7b97d",
        "鬼脸": "def52",
        "跳舞": "741d5",
        "男孩": "46b8e",
        "奸笑": "289dc",
        "猪": "6935b",
        "圈": "3ece0",
        "便便": "462db",
        "外星": "0a22b",
        "圣诞": "8e7",
        "流泪": "01000",
        "强": "1",
        "爱心": "0CoJU",
        "女孩": "m6Qyw",
        "惊恐": "8W8ju",
        "大笑": "d"
    };


