var dc

!function(t) {
    var e = {};
    function r(n) {
        if (e[n])
            return e[n].exports;
        var o = e[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return t[n].call(o.exports, o, o.exports, r),
            o.l = !0,
            o.exports
    }
    r.m = t,
        r.c = e,
        r.d = function(t, e, n) {
            r.o(t, e) || Object.defineProperty(t, e, {
                enumerable: !0,
                get: n
            })
        }
        ,
        r.r = function(t) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(t, "__esModule", {
                    value: !0
                })
        }
        ,
        r.t = function(t, e) {
            if (1 & e && (t = r(t)),
            8 & e)
                return t;
            if (4 & e && "object" == typeof t && t && t.__esModule)
                return t;
            var n = Object.create(null);
            if (r.r(n),
                Object.defineProperty(n, "default", {
                    enumerable: !0,
                    value: t
                }),
            2 & e && "string" != typeof t)
                for (var o in t)
                    r.d(n, o, function(e) {
                        return t[e]
                    }
                        .bind(null, o));
            return n
        }
        ,
        r.n = function(t) {
            var e = t && t.__esModule ? function() {
                        return t.default
                    }
                    : function() {
                        return t
                    }
            ;
            return r.d(e, "a", e),
                e
        }
        ,
        r.o = function(t, e) {
            return Object.prototype.hasOwnProperty.call(t, e)
        }
        ,
        r.p = "",
        r(r.s = 29)
}({
    29: function(t, e) {
        function r(t) {
            return (r = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(t) {
                        return typeof t
                    }
                    : function(t) {
                        return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
                    }
            )(t)
        }
        function n(t, e) {
            n = function(t, e) {
                return new l(t,void 0,e)
            }
            ;
            var i = u(RegExp)
                , c = RegExp.prototype
                , f = new WeakMap;
            function l(t, e, r) {
                var n = i.call(this, t, e);
                return f.set(n, r || f.get(t)),
                    n
            }
            function p(t, e) {
                var r = f.get(e);
                return Object.keys(r).reduce((function(e, n) {
                        return e[n] = t[r[n]],
                            e
                    }
                ), Object.create(null))
            }
            return o(l, i),
                l.prototype.exec = function(t) {
                    var e = c.exec.call(this, t);
                    return e && (e.groups = p(e, this)),
                        e
                }
                ,
                l.prototype[Symbol.replace] = function(t, e) {
                    if ("string" == typeof e) {
                        var n = f.get(this);
                        return c[Symbol.replace].call(this, t, e.replace(/\$<([^>]+)>/g, (function(t, e) {
                                return "$" + n[e]
                            }
                        )))
                    }
                    if ("function" == typeof e) {
                        var o = this;
                        return c[Symbol.replace].call(this, t, (function() {
                                var t = [];
                                return t.push.apply(t, arguments),
                                "object" !== r(t[t.length - 1]) && t.push(p(t, o)),
                                    e.apply(this, t)
                            }
                        ))
                    }
                    return c[Symbol.replace].call(this, t, e)
                }
                ,
                n.apply(this, arguments)
        }
        function o(t, e) {
            if ("function" != typeof e && null !== e)
                throw new TypeError("Super expression must either be null or a function");
            t.prototype = Object.create(e && e.prototype, {
                constructor: {
                    value: t,
                    writable: !0,
                    configurable: !0
                }
            }),
            e && c(t, e)
        }
        function u(t) {
            var e = "function" == typeof Map ? new Map : void 0;
            return (u = function(t) {
                    if (null === t || (r = t,
                    -1 === Function.toString.call(r).indexOf("[native code]")))
                        return t;
                    var r;
                    if ("function" != typeof t)
                        throw new TypeError("Super expression must either be null or a function");
                    if (void 0 !== e) {
                        if (e.has(t))
                            return e.get(t);
                        e.set(t, n)
                    }
                    function n() {
                        return i(t, arguments, f(this).constructor)
                    }
                    return n.prototype = Object.create(t.prototype, {
                        constructor: {
                            value: n,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                        c(n, t)
                }
            )(t)
        }
        function i(t, e, r) {
            return (i = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Date.prototype.toString.call(Reflect.construct(Date, [], (function() {}
                        ))),
                            !0
                    } catch (t) {
                        return !1
                    }
                }() ? Reflect.construct : function(t, e, r) {
                    var n = [null];
                    n.push.apply(n, e);
                    var o = new (Function.bind.apply(t, n));
                    return r && c(o, r.prototype),
                        o
                }
            ).apply(null, arguments)
        }
        function c(t, e) {
            return (c = Object.setPrototypeOf || function(t, e) {
                    return t.__proto__ = e,
                        t
                }
            )(t, e)
        }
        function f(t) {
            return (f = Object.setPrototypeOf ? Object.getPrototypeOf : function(t) {
                    return t.__proto__ || Object.getPrototypeOf(t)
                }
            )(t)
        }
        dc = function(o, u, bookshelfHref) {
            var e;
            var r;
            if (void 0 === o || void 0 === u)
                throw new TypeError("The following required keys may be missing: Path, Content");
            if (!/\.xht(ml)?$/i.test(o))
                return u;

            var nRes = n(/bibi\x2Dbookshelf\x2D([0-9a-f]{50})/, {
                k: 1
            })
            var i = (null === (r = bookshelfHref.match(n(/bibi\x2Dbookshelf\x2D([0-9a-f]{50})/, {
                k: 1
            }))) || void 0 === r ? void 0 : r.groups.k) + "94f885c659"
            console.log(" ", "0---------+---------+---------+---------+---------+---------")
            console.log("i", i)
            var c = Array.from({
                length: 10
            }).map((function(_, e) {
                    return parseInt(Array.from({
                        length: 6
                    }).map((function(_, r) {
                            var isub = i.substring(e + 10 * r, e + 10 * r + 1)
                            console.log("start:", e + 10 * r, "end:", e + 10 * r + 1, "isub:", isub)
                            return isub
                        }
                    )).join(""), 16) % parseInt("10FFFF", 16)
                }
            ));
            console.log("c", c)
            return u.replace(/U\+([0-f]{6})([0-9]);/g, (function(t, e, r) {
                    return String.fromCodePoint(parseInt(e, 16) ^ c[r])
                }
            ))
        }
    }
});

u = `
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" class="hltr">
<head>
<meta charset="utf-8" />
<title>U+10a2019;U+0f4fa01;U+0399068;U+0aba216;U+02eac44;U+10e0ca9;U+03232d8;</title>
<link rel="stylesheet" type="text/css" href="../style/book-style.css" />
</head>

<body class="p-image">
<div class="main">
<div class="align-center"><p><img alt="" class="fit" src="../image/i-000b_01.jpg" /></p></div>
</div>
</body>

</html>
`

bookshelfHref = "https://jbungakukan.shogakukan.co.jp/bibi-bookshelf-6968781cfb976892be1a676e928da9df3e92ae9295de47dca9";


var foo = dc("item/xhtml/p-0002.xhtml", u, bookshelfHref)
console.log(foo)


console.log(parseInt("696d99", 16))
console.log(parseInt("696d99", 16) % parseInt("10FFFF", 16))


